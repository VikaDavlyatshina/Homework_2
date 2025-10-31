import json
import os

import pytest

from src.category import Category
from src.product import LawnGrass, Product, Smartphone


@pytest.fixture
def sample_product():
    """Базовый тестовый товар"""
    return Product("Футболка", "Хлопковая футболка", 99.99, 10)


@pytest.fixture
def second_product():
    """Второй тестовый товар"""
    return Product("Джинсы", "Синие джинсы", 149.99, 15)


@pytest.fixture
def sample_products(sample_product, second_product):
    """Список тестовых товаров (использует другие фикстуры)"""
    return [sample_product, second_product]


@pytest.fixture
def electronic_product():
    """Товар для электроники"""
    return Product("Смартфон", "Флагманский смартфон", 50000.0, 5)


@pytest.fixture
def clothing_category(sample_products):
    """Категория одежды с товарами"""
    return Category("Одежда", "Модная одежда", sample_products)


@pytest.fixture
def electronics_category(electronic_product):
    """Категория электроники с одним товаром"""
    return Category("Электроника", "Техника", [electronic_product])


"""Фикстуры для данных (словари)"""


@pytest.fixture
def product_dict():
    """Данные товара в виде словаря"""
    return {"name": "Телефон", "description": "Смартфон", "price": 20000.0, "quantity": 5}


@pytest.fixture
def duplicate_product_dict(sample_product):
    """Данные товара-дубликата"""
    return {
        "name": sample_product.name,  # Такое же имя как у sample_product
        "description": "Новое описание",
        "price": 150.0,  # Другая цена
        "quantity": 3,  # Другое количество
    }


@pytest.fixture
def smartphone_product():
    """Фикстура для создания смартфона"""
    return Smartphone(
        name="iPhone 15",
        description="Новый смартфон Apple",
        price=999.99,
        quantity=5,
        efficiency="A16 Bionic",
        model="15 Pro",
        memory=256,
        color="Black",
    )


@pytest.fixture
def lawn_grass_product():
    """Фикстура для создания газонной травы"""
    return LawnGrass(
        name="Газонная трава Премиум",
        description="Мягкая газонная трава",
        price=49.99,
        quantity=100,
        country="Россия",
        germination_period=14,
        color="Зеленый",
    )


@pytest.fixture
def second_smartphone():
    """Второй смартфон для тестов сложения"""
    return Smartphone(
        name="Samsung Galaxy",
        description="Android smartphone",
        price=799.99,
        quantity=3,
        efficiency="Snapdragon",
        model="S23",
        memory=128,
        color="White",
    )


@pytest.fixture
def second_lawn_grass():
    """Вторая газонная трава для тестов сложения"""
    return LawnGrass(
        name="Газонная трава Стандарт",
        description="Обычная газонная трава",
        price=29.99,
        quantity=50,
        country="Беларусь",
        germination_period=10,
        color="Светло-зеленый",
    )


"""Фикстуры для Json"""


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


@pytest.fixture
def valid_json_data():
    """Валидные данные в виде словаря (без файла)"""
    return [
        {
            "name": "Одежда",
            "description": "Модная одежда",
            "products": [{"name": "Футболка", "description": "Хлопковая", "price": 99.99, "quantity": 10}],
        }
    ]


@pytest.fixture
def json_data_with_missing_fields():
    """Данные с отсутствующими обязательными полями"""
    return [
        {
            "name": "Одежда",
            # Нет description - обязательное поле
            "products": [{"name": "Футболка", "description": "Хлопковая", "price": 99.99, "quantity": 10}],
        }
    ]


@pytest.fixture
def empty_data():
    """Пустые данные"""
    return []
