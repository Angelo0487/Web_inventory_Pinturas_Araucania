import argparse
from flask import Flask, render_template, redirect, url_for, flash
from database import db, create_app
from models import Product, Movement
from forms import MovementForm

app = create_app()

# ----------- RUTA PRINCIPAL -----------
@app.route('/')
def index():
    valuation_cost = db.session.query(db.func.sum(Product.stock * Product.cost_price)).scalar() or 0
    valuation_sale = db.session.query(db.func.sum(Product.stock * Product.sale_price)).scalar() or 0
    low_stock = Product.query.filter(Product.stock <= Product.min_stock).count()
    total_products = Product.query.count()
    total_stock = db.session.query(db.func.sum(Product.stock)).scalar() or 0
    last_movs = Movement.query.order_by(Movement.created_at.desc()).limit(10).all()

    return render_template(
        'dashboard.html',
        valuation_cost=valuation_cost,
        valuation_sale=valuation_sale,
        low_stock=low_stock,
        total_products=total_products,
        total_stock=total_stock,
        last_movs=last_movs
    )

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
        return redirect(url_for('index'))

    return render_template('movement_form.html', form=form)

# ----------- REPORTES -----------
@app.route('/reports/low-stock')
def report_low_stock():
    products = Product.query.filter(Product.stock <= Product.min_stock).order_by(Product.stock.asc()).all()
    return render_template('reports_low_stock.html', products=products)

@app.route('/reports/valuation')
def report_valuation():
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

    app.run(debug=True, host="0.0.0.0", port=5001)
