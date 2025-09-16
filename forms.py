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
    sku = StringField('SKU', validators=[DataRequired()])
    name = StringField('Nombre', validators=[DataRequired()])
    category = StringField('Categoría', validators=[Optional()])
    description = TextAreaField('Descripción', validators=[Optional()])
    cost_price = FloatField('Precio compra', validators=[NumberRange(min=0)], default=0)
    sale_price = FloatField('Precio venta', validators=[NumberRange(min=0)], default=0)
    stock = IntegerField('Stock', validators=[NumberRange(min=0)], default=0)
    min_stock = IntegerField('Stock mínimo', validators=[NumberRange(min=0)], default=0)
    supplier_id = SelectField('Proveedor', coerce=int, validators=[Optional()])
    submit = SubmitField('Guardar')

class SupplierForm(FlaskForm):
    name = StringField('Nombre', validators=[DataRequired()])
    email = StringField('Correo', validators=[Optional()])
    phone = StringField('Teléfono', validators=[Optional()])
    address = StringField('Dirección', validators=[Optional()])
    submit = SubmitField('Guardar')

class MovementForm(FlaskForm):
    product_id = SelectField('Producto', coerce=int, validators=[DataRequired()])
    kind = SelectField('Tipo', choices=[('IN', 'Entrada'), ('OUT', 'Salida')], validators=[DataRequired()])
    quantity = IntegerField('Cantidad', validators=[DataRequired(), NumberRange(min=1)])
    note = StringField('Nota', validators=[Optional()])
    submit = SubmitField('Registrar movimiento')