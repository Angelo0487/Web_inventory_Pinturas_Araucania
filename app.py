import argparse
from flask import Flask, render_template, redirect, url_for, flash, request
from database import db, create_app
from models import Product, Movement
from forms import MovementForm

app = create_app()

# ----------- MOVIMIENTOS -----------
@app.route('/movement/new', methods=['GET', 'POST'])
def movement_form():
    form = MovementForm()
    if form.validate_on_submit():
        product = Product.query.get(form.product_id.data)
        kind = form.kind.data
        qty = form.quantity.data

        mov = Movement(product_id=product.id, kind=kind, quantity=qty, note=form.note.data)
        db.session.add(mov)

        # Actualiza stock
        if kind == 'IN':
            product.stock += qty
        else:
            product.stock -= qty

        db.session.commit()
        flash('Movimiento registrado', 'success')
        return redirect(url_for('movements_list'))

    return render_template('movement_form.html', form=form)

# ----------- REPORTES -----------
@app.route('/reports/low-stock')
def report_low_stock():
    products = Product.query.filter(Product.stock <= Product.min_stock).order_by(Product.stock.asc()).all()
    return render_template('reports_low_stock.html', products=products)

@app.route('/reports/valuation')
def report_valuation():
    # Totales
    total_cost = db.session.query(db.func.sum(Product.stock * Product.cost_price)).scalar() or 0
    total_sale = db.session.query(db.func.sum(Product.stock * Product.sale_price)).scalar() or 0
    products = Product.query.order_by(Product.name.asc()).all()
    return render_template('reports_valuation.html', products=products, total_cost=total_cost, total_sale=total_sale)

# ----------- MAIN -----------
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--init-db', action='store_true')
    args = parser.parse_args()

    with app.app_context():
        if args.init_db:
            db.create_all()
            print('Base de datos inicializada.')

    app.run(debug=True)