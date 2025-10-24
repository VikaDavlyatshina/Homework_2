import pytest

from src.product import  Product
from src.category import Category

@pytest.fixture
def first_category():
    return Category(
        name="Одежда",
        description="Модная одежда",
        products=[
            Product("Футболка", "Хлопковая футболка", 99.99, 10),
            Product("Джинсы", "Синие джинсы", 149.99, 15)
        ]
    )

@pytest.fixture
def second_category():
    return Category(
        name="Книги",
        description="Книги и учебники",
        products=[
            Product("Учебник", "Учебная литература", 50.99, 5),
            Product("Научная фантастика", "Фантастика", 70.99, 10),
            Product("Книга", "Художественная литература", 69.99, 7)
        ]
    )

@pytest.fixture
def product():
    return Product("Футболка", "Хлопковая футболка", 99.99, 10)