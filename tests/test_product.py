import pytest
from src.product import Product

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
