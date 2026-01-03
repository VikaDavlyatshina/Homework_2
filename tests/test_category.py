import pytest

from src.category import Category
from src.product import Product

"""Тест для класса Category"""


def test_category_init(clothing_category):
    """Тест инициализации категории"""
    assert clothing_category.name == "Одежда"
    assert clothing_category.description == "Модная одежда"

    products_str = clothing_category.products
    assert "Футболка" in products_str
    assert "Джинсы" in products_str


def test_category_products_format(clothing_category):
    products_output = clothing_category.products

    assert "Футболка, 99.99 руб. Остаток: 10 шт." in products_output
    assert "Джинсы, 149.99 руб. Остаток: 15 шт." in products_output


def test_empty_category():
    """Тест: можно создать категорию без товаров"""
    empty_category = Category("Электроника", "Техника", [])

    assert empty_category.name == "Электроника"
    assert empty_category.products == "В этой категории пока нет товаров"


def test_total_product_count():
    """Тестируем счетчик товаров"""
    Category.category_count = 0
    Category.product_count = 0

    Category(
        "Одежда",
        "Модная одежда",
        [Product("Футболка", "Хлопковая футболка", 100.00, 10), Product("Джинсы", "Синие джинсы", 150.00, 15)],
    )

    Category(
        "Книги",
        "Книги и учебники",
        [
            Product("Учебник", "Учебная литература", 50.99, 5),
            Product("Научная фантастика", "Фантастика", 70.99, 10),
            Product("Книга", "Художественная литература", 69.99, 7),
        ],
    )

    assert Category.category_count == 2
    assert Category.product_count == 5


def test_add_product_to_category(clothing_category, capsys):
    new_product = Product("Куртка", "Зимняя куртка", 299.99, 3)

    initial_count = Category.product_count

    clothing_category.add_product(new_product)

    captured = capsys.readouterr()
    assert "Товар 'Куртка' добавлен в категорию 'Одежда'" in captured.out

    products_output = clothing_category.products
    assert "Куртка, 299.99 руб. Остаток: 3 шт." in products_output
    assert Category.product_count == initial_count + 1


def test_category_str_representation(clothing_category):
    """Тест строкового представления категории"""
    result = str(clothing_category)
    expected = "Одежда, количество продуктов: 25 шт."  # 10 + 15
    assert result == expected


def test_add_smartphone_to_category(clothing_category, smartphone_product, capsys):
    """Тест добавления смартфона в категорию."""
    initial_count = Category.product_count

    clothing_category.add_product(smartphone_product)

    # Проверяем сообщение о добавлении
    captured = capsys.readouterr()
    assert f"Товар '{smartphone_product.name}' добавлен в категорию '{clothing_category.name}'" in captured.out

    # Проверяем, что счетчик увеличился
    assert Category.product_count == initial_count + 1

    # Проверяем, что товар действительно добавлен
    products_output = clothing_category.products
    assert "iPhone 15" in products_output


def test_add_lawn_grass_to_category(clothing_category, lawn_grass_product, capsys):
    """
    Тест добавления газонной травы в категорию.
    Должно работать, так как LawnGrass наследуется от Product.
    """
    initial_count = Category.product_count

    clothing_category.add_product(lawn_grass_product)

    captured = capsys.readouterr()
    assert f"Товар '{lawn_grass_product.name}' добавлен в категорию '{clothing_category.name}'" in captured.out
    assert Category.product_count == initial_count + 1

    products_output = clothing_category.products
    assert "Газонная трава Премиум" in products_output


def test_add_invalid_product_raises_error(clothing_category):
    """
    Тест, что попытка добавить не-продукт вызывает TypeError.
    """
    with pytest.raises(TypeError) as exc_info:
        clothing_category.add_product("Это строка, а не продукт")

    assert "Можно добавлять только объекты класса Product и его наследников!" in str(exc_info.value)


def test_add_integer_raises_error(clothing_category):
    """
    Тест с числом вместо продукта.
    """
    with pytest.raises(TypeError) as exc_info:
        clothing_category.add_product(123)

    assert "Можно добавлять только объекты класса Product и его наследников!" in str(exc_info.value)


def test_add_none_raises_error(clothing_category):
    """
    Тест с None вместо продукта.
    """
    with pytest.raises(TypeError) as exc_info:
        clothing_category.add_product(None)

    assert "Можно добавлять только объекты класса Product и его наследников!" in str(exc_info.value)


def test_middle_price_empty_category():
    """Пустая категория должна возвращать 0"""
    category = Category("Пустая категория", "Категория без товара")
    assert category.middle_price() == 0


def test_middle_price_category(sample_products, clothing_category):
    """Тест вычисления средней цены"""
    assert clothing_category.middle_price() == 124.99
