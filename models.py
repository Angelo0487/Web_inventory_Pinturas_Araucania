from datetime import datetime
from database import db

class Supplier(db.Model):
    __tablename__ = 'suppliers'
id = db.Column(db.Integer, primary_key=True)
name = db.Column(db.String(120), nullable=False)
email = db.Column(db.String(120))
phone = db.Column(db.String(50))
address = db.Column(db.String(200))
created_at = db.Column(db.DateTime, default=datetime.utcnow)

products = db.relationship('Product', backref='supplier', lazy=True)

def __repr__(self):
    return f"<Supplier {self.name}>"

class Product(db.Model):
    __tablename__ = 'products'
id = db.Column(db.Integer, primary_key=True)
sku = db.Column(db.String(50), unique=True, nullable=False)
name = db.Column(db.String(150), nullable=False)
category = db.Column(db.String(100))
description = db.Column(db.Text)
cost_price = db.Column(db.Float, default=0.0)
sale_price = db.Column(db.Float, default=0.0)
stock = db.Column(db.Integer, default=0)
min_stock = db.Column(db.Integer, default=0)
supplier_id = db.Column(db.Integer, db.ForeignKey('suppliers.id'))
created_at = db.Column(db.DateTime, default=datetime.utcnow)

def __repr__(self):
    return f"<Product {self.sku} - {self.name}>"


class Movement(db.Model):
    __tablename__ = 'movements'
id = db.Column(db.Integer, primary_key=True)
product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
kind = db.Column(db.String(10), nullable=False) # 'IN' o 'OUT'
quantity = db.Column(db.Integer, nullable=False)
note = db.Column(db.String(200))
created_at = db.Column(db.DateTime, default=datetime.utcnow)

product = db.relationship('Product', backref='movements', lazy=True)

def __repr__(self):
    return f"<Movement {self.kind} x{self.quantity} product={self.product_id}>"