from sqlalchemy import Column, Integer, Float , String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app import db

class Salebase(db.Model):
    __abstract__ = True

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)


class Category(Salebase):
    __tablename__='Category'
    products = relationship('Product', backref='category', lazy=True)


class Product(Salebase):
    description = Column(String(255))
    price = Column(Float, default=0)
    image = Column(String(100))

    category_id= Column(Integer, ForeignKey(Category.id), nullable=False)