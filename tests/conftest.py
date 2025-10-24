import json
import os

import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def sample_products():
    return [Product("Футболка", "Хлопковая футболка", 99.99, 10), Product("Джинсы", "Синие джинсы", 149.99, 15)]


@pytest.fixture
def first_category(sample_products):
    return Category(name="Одежда", description="Модная одежда", products=sample_products)


@pytest.fixture
def second_category():
    return Category(
        name="Книги",
        description="Книги и учебники",
        products=[
            Product("Учебник", "Учебная литература", 50.99, 5),
            Product("Научная фантастика", "Фантастика", 70.99, 10),
            Product("Книга", "Художественная литература", 69.99, 7),
        ],
    )


@pytest.fixture
def product():
    return Product("Футболка", "Хлопковая футболка", 99.99, 10)


@pytest.fixture
def product_data():
    return {"name": "Телефон", "description": "Смартфон", "price": 20000, "quantity": 5}


@pytest.fixture
def create_test_json_file():
    test_data = [
        {
            "name": "Одежда",
            "description": "Модная одежда",
            "products": [
                {"name": "Футболка", "description": "Хлопковая футболка", "price": 99.99, "quantity": 10},
                {"name": "Джинсы", "description": "Синие джинсы", "price": 149.99, "quantity": 5},
            ],
        }
    ]

    # Сохраняем данные в
    with open("test_products.json", "w", encoding="UTF-8") as f:
        json.dump(test_data, f, ensure_ascii=False, indent=2)

    # Возвращаем имя файла для использования в тестах
    yield "test_products.json"

    # Удаляем файл после теста
    if os.path.exists("test_products.json"):
        os.remove("test_products.json")


@pytest.fixture
def create_empty_json_file():
    with open("test_empty.json", "w", encoding="UTF-8") as f:
        json.dump([], f)

    yield "test_empty.json"

    if os.path.exists("test_empty.json"):
        os.remove("test_empty.json")


@pytest.fixture
def create_invalid_json_file():
    with open("test_invalid.json", "w", encoding="UTF-8") as f:
        f.write("это не JSON {]")

    yield "test_invalid.json"

    if os.path.exists("test_invalid.json"):
        os.remove("test_invalid.json")
