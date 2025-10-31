from src.product import Product
from tests.conftest import lawn_grass_product
import pytest

"""Тесты для класса Product"""


def test_product_init(sample_product):
    assert sample_product.name == "Футболка"
    assert sample_product.description == "Хлопковая футболка"
    assert sample_product.price == 99.99
    assert sample_product.quantity == 10


def test_product_attributes():
    book = Product("Книга", "Интересная книга", 129.99, 15)

    assert book.name == "Книга"
    assert book.description == "Интересная книга"
    assert book.price == 129.99
    assert book.quantity == 15


def test_price_setter_negative(sample_product, capsys):
    sample_product.price = -50
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out
    assert sample_product.price == 99.99


def test_price_setter_zero(sample_product, capsys):
    sample_product.price = 0
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out
    assert sample_product.price == 99.99


def test_price_setter_positive(sample_product):
    """Тест установки корректной цены"""
    sample_product.price = 150.0
    assert sample_product.price == 150.0


def test_new_product_without_duplicates(product_dict, sample_product):
    """Тест создания товара без дубликатов"""
    new_product = Product.new_product(product_dict, [sample_product])
    assert new_product.name == "Телефон"  # Новый товар
    assert new_product.quantity == 5


def test_new_product_without_list(product_dict):
    """Тест создания товара без передачи списка"""
    new_product = Product.new_product(product_dict)
    assert new_product.name == "Телефон"
    assert new_product.quantity == 5


def test_product_str_representation(sample_product):
    """Тест строкового представления товара"""
    result = str(sample_product)
    expected = "Футболка, 99.99 руб. Остаток: 10 шт."
    assert result == expected


def test_product_addition(sample_product, second_product):
    """Тест сложения товаров"""
    total = sample_product + second_product
    expected = (99.99 * 10) + (149.99 * 15)
    assert total == expected


def test_product_addition_different_types(sample_product, electronic_product):
    """Тест сложения товаров разных типов (должно работать, так как оба Product)"""
    total = sample_product + electronic_product
    expected = (99.99 * 10) + (50000.0 * 5)
    assert total == expected

def test_smartphone_init(smartphone_product):
    """Тест инициализации смартфона. Проверяем, что все атрибуты установлены правильно."""
    # Проверяем наследуемые атрибуты (от Product)
    assert smartphone_product.name == "iPhone 15"
    assert smartphone_product.description == "Новый смартфон Apple"
    assert smartphone_product.price == 999.99
    assert smartphone_product.quantity == 5

    # Проверяем специфические атрибуты смартфона
    assert smartphone_product.efficiency == "A16 Bionic"
    assert smartphone_product.model == "15 Pro"
    assert smartphone_product.memory == 256
    assert smartphone_product.color == "Black"

def test_smartphone_str(smartphone_product):
    """Тест строкового представления смартфона.
    Проверяем, что выводится базовая и специфическая информация"""
    result = str(smartphone_product)

    # Проверяем базовую информацию (наследуемую от Product)
    assert "iPhone 15" in result
    assert "999.99 руб." in result
    assert "Остаток: 5 шт." in result

    # Проверяем специфическую информацию смартфона
    assert "A16 Bionic" in result
    assert "15 Pro" in result
    assert "256 ГБ" in result
    assert "Black" in result

def test_lawn_grass_init(lawn_grass_product):
    """
    Тест инициализации газонной травы
    """
    # Наследуемые атрибуты
    assert lawn_grass_product.name == "Газонная трава Премиум"
    assert lawn_grass_product.description == "Мягкая газонная трава"
    assert lawn_grass_product.price == 49.99
    assert lawn_grass_product.quantity == 100

    # Специфические атрибуты газонной травы
    assert lawn_grass_product.country == "Россия"
    assert lawn_grass_product.germination_period == 14
    assert lawn_grass_product.color == "Зеленый"


def test_lawn_grass_str_representation(lawn_grass_product):
    """
    Тест строкового представления газонной травы.
    """
    result = str(lawn_grass_product)

    # Базовая информация
    assert "Газонная трава Премиум" in result
    assert "49.99 руб." in result
    assert "Остаток: 100 шт." in result

    # Специфическая информация
    assert "Россия" in result
    assert "Срок прорастания: 14" in result
    assert "Зеленый" in result

def test_smartphone_addition_same_class(smartphone_product, second_smartphone):
    """Тест сложения двух смартфонов"""
    total = smartphone_product + second_smartphone

    # Ожидаемый результат: (цена1 * количество1) + (цена2 * количество2)
    expected = (999.99 * 5) + (799.99 * 3)
    assert total == expected

def test_lawn_grass_addition_same_class(lawn_grass_product, second_lawn_grass):
    """Тест сложения двух газонных трав"""
    total = lawn_grass_product + second_lawn_grass
    expected = (49.99 * 100) + (29.99 * 50)
    assert total == expected


def test_addition_different_classes_raises_error(smartphone_product, lawn_grass_product):
    """Тест, что сложение разных классов вызывает TypeError."""
    # Используем параметр match для проверки текста ошибки
    with pytest.raises(TypeError, match="Можно складывать только товары из одинаковых классов продуктов"):
        result = smartphone_product + lawn_grass_product


def test_addition_product_with_smartphone_raises_error(sample_product, smartphone_product):
    """Тест, что сложение Product и Smartphone вызывает ошибку."""
    with pytest.raises(TypeError, match="Можно складывать только товары из одинаковых классов продуктов"):
       result=  sample_product + smartphone_product


def test_addition_product_with_lawn_grass_raises_error(sample_product, lawn_grass_product):
    """Тест, что сложение Product и LawnGrass вызывает ошибку."""
    with pytest.raises(TypeError, match="Можно складывать только товары из одинаковых классов продуктов"):
        result = sample_product + lawn_grass_product