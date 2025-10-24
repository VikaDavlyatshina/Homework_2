import pytest

from src.product import  Product
from src.category import Category

@pytest.fixture
def sample_products():
    """Фикстура с образцами товаров"""
    return [
        Product("Футболка", "Хлопковая футболка", 99.99, 10),
        Product("Джинсы", "Синие джинсы", 149.99, 15)
    ]

@pytest.fixture
def first_category(sample_products):
    return Category(
        name="Одежда",
        description="Модная одежда",
        products=sample_products
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

@pytest.fixture
def product_data():
    return {
            'name': 'Телефон',
            'description': 'Смартфон',
            'price': 20000,
            'quantity': 5
        }