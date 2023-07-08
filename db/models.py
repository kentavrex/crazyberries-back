from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.sql import func

from db.helpers import ProductCardStatus


Base = declarative_base()


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True, unique=True)
    login = Column(String(50), nullable=False, unique=True)
    name = Column(String(50), nullable=False)
    location = Column(String(50), nullable=False)


users = User.__table__


class Comment(Base):
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())
    author_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    product_card_id = Column(Integer, ForeignKey("product_card.id"), nullable=False)
    text = Column(String(1000), nullable=False)

    author = relationship("User", foreign_keys=[author_id])
    product_card = relationship("ProductCard")


comment = Comment.__table__


class ProductCard(Base):
    __tablename__ = "product_card"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(80), nullable=False)
    price = Column(Integer, nullable=False)
    author_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    category = Column(String(100), nullable=False)
    description = Column(String(100), nullable=True)
    status = Column(String(100), default=ProductCardStatus.new, nullable=False)

    author = relationship("User", foreign_keys=[author_id])


product_card = ProductCard.__table__
