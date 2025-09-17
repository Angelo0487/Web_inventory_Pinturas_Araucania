from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    TextAreaField,
    FloatField,
    IntegerField,
    SelectField,
    SubmitField
)
from wtforms.validators import DataRequired, NumberRange, Optional

class ProductForm(FlaskForm):
    sku = StringField('SKU', validators=[DataRequired()], default='')
    name = StringField('Nombre', validators=[DataRequired()], default='')
    category = StringField('Categoría', validators=[Optional()], default='')
    description = TextAreaField('Descripción', validators=[Optional()], default='', render_kw={"rows": 3})
    cost_price = FloatField('Precio compra', validators=[NumberRange(min=0)], default=0)
    sale_price = FloatField('Precio venta', validators=[NumberRange(min=0)], default=0)
    stock = IntegerField('Stock', validators=[NumberRange(min=0)], default=0)
    min_stock = IntegerField('Stock mínimo', validators=[NumberRange(min=0)], default=0)
    supplier_id = SelectField('Proveedor', coerce=int, validators=[Optional()])
    submit = SubmitField('Guardar')

class SupplierForm(FlaskForm):
    name = StringField('Nombre', validators=[DataRequired()], default='')
    email = StringField('Correo', validators=[Optional()], default='')
    phone = StringField('Teléfono', validators=[Optional()], default='')
    address = StringField('Dirección', validators=[Optional()], default='')
    submit = SubmitField('Guardar')

class MovementForm(FlaskForm):
    product_id = SelectField('Producto', coerce=int, validators=[DataRequired()])
    kind = SelectField('Tipo', choices=[('IN', 'Entrada'), ('OUT', 'Salida')], validators=[DataRequired()])
    quantity = IntegerField('Cantidad', validators=[DataRequired(), NumberRange(min=1)], default=1)
    note = StringField('Nota', validators=[Optional()], default='')
    submit = SubmitField('Registrar movimiento')