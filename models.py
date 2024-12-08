from typing import List, Optional, Annotated

from fastapi import Depends
from sqlalchemy import Column, ForeignKey, Index, Integer, LargeBinary, Text, create_engine
from sqlalchemy.orm import Mapped, declarative_base, mapped_column, relationship, sessionmaker
from sqlalchemy.orm.base import Mapped

Base = declarative_base()
metadata = Base.metadata

engine = create_engine('sqlite:///ecommerce.db')
Session = sessionmaker(bind=engine, autocommit=False, autoflush=False)







class Users(Base):
    __tablename__ = 'Users'

    Id = mapped_column(Integer, primary_key=True)
    UserName = mapped_column(Text, nullable=False)
    Role = mapped_column(Text, nullable=False)
    PasswordSalt = mapped_column(LargeBinary, nullable=False)
    HashedPassword = mapped_column(LargeBinary, nullable=False)

    Categories: Mapped[List['Categories']] = relationship('Categories', uselist=True, back_populates='Users_')
    Orders: Mapped[List['Orders']] = relationship('Orders', uselist=True, foreign_keys='[Orders.CustomerId]', back_populates='Users_')
    Orders_: Mapped[List['Orders']] = relationship('Orders', uselist=True, foreign_keys='[Orders.HandlerId]', back_populates='Users1')





class Categories(Base):
    __tablename__ = 'Categories'
    __table_args__ = (
        Index('IX_Categories_Name', 'Name', unique=True),
        Index('IX_Categories_UserId', 'UserId')
    )

    Id = mapped_column(Integer, primary_key=True)
    Name = mapped_column(Text, nullable=False)
    UserId = mapped_column(ForeignKey('Users.Id', ondelete='CASCADE'), nullable=False)
    Description = mapped_column(Text)

    Users_: Mapped['Users'] = relationship('Users', back_populates='Categories')
    Products: Mapped[List['Products']] = relationship('Products', uselist=True, back_populates='Categories_')


class Orders(Base):
    __tablename__ = 'Orders'
    __table_args__ = (
        Index('IX_Orders_CustomerId', 'CustomerId'),
        Index('IX_Orders_HandlerId', 'HandlerId')
    )

    Id = mapped_column(Integer, primary_key=True)
    CreatedDate = mapped_column(Text, nullable=False)
    State = mapped_column(Text, nullable=False)
    CustomerId = mapped_column(ForeignKey('Users.Id'), nullable=False)
    ConfirmedDate = mapped_column(Text)
    RemovedDate = mapped_column(Text)
    HandlerId = mapped_column(ForeignKey('Users.Id'))

    Users_: Mapped['Users'] = relationship('Users', foreign_keys=[CustomerId], back_populates='Orders')
    Users1: Mapped[Optional['Users']] = relationship('Users', foreign_keys=[HandlerId], back_populates='Orders_')
    OrdersProducts: Mapped[List['OrdersProducts']] = relationship('OrdersProducts', uselist=True, back_populates='Orders_')


class Products(Base):
    __tablename__ = 'Products'
    __table_args__ = (
        Index('IX_Products_CategoryId', 'CategoryId'),
    )

    Id = mapped_column(Integer, primary_key=True)
    Name = mapped_column(Text, nullable=False)
    CategoryId = mapped_column(ForeignKey('Categories.Id', ondelete='CASCADE'), nullable=False)
    UnitPrice = mapped_column(Integer, nullable=False)
    Description = mapped_column(Text)

    Categories_: Mapped['Categories'] = relationship('Categories', back_populates='Products')
    OrdersProducts: Mapped[List['OrdersProducts']] = relationship('OrdersProducts', uselist=True, back_populates='Products_')


class OrdersProducts(Base):
    __tablename__ = 'OrdersProducts'
    __table_args__ = (
        Index('IX_OrdersProducts_ProductId', 'ProductId'),
    )

    OrderId = mapped_column(ForeignKey('Orders.Id', ondelete='CASCADE'), primary_key=True, nullable=False)
    ProductId = mapped_column(ForeignKey('Products.Id', ondelete='CASCADE'), primary_key=True, nullable=False)
    UnitCount = mapped_column(Integer, nullable=False)
    UnitPrice = mapped_column(Integer, nullable=False)

    Orders_: Mapped['Orders'] = relationship('Orders', back_populates='OrdersProducts')
    Products_: Mapped['Products'] = relationship('Products', back_populates='OrdersProducts')



def get_db_conn():
    session = None
    try:
        session = Session()
        yield session
    finally:
        session.close()






Db = Annotated[Session, Depends(get_db_conn)]