"""Util classes for db models"""
from enum import Enum


class ProductCardStatus(Enum):
    new = "Новое"
    closed = "Закрыто"
    available = "Доступно для покупки"
    out_of_stock = "Распродано"


class ProductCardCategory(Enum):
    clothes = "Clothes"
    toys = "Toys"
    home = "Home"
    male = "Male"
    female = "Female"
    kids = "Kids"
    shoes = "Shoes"
