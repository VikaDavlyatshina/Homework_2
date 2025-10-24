from src.category import Category
from src.product import Product

"""Тест для класса Category"""

def test_category_init(first_category, second_category):
    """Тест инициализации"""
    assert first_category.name == "Одежда"
    assert first_category.description == "Модная одежда"

    assert len(first_category.products) == 2
    assert len(second_category.products) == 3


def test_category_products(first_category):
    assert first_category.products[0].name == "Футболка"
    assert first_category.products[0].price == 99.99

    assert first_category.products[1].name == "Джинсы"
    assert first_category.products[1].price == 149.99

def test_empty_category():
    """Тест: можно создать категорию без товаров"""
    empty_category = Category("Электроника", "Техника", [])

    assert empty_category.name == "Электроника"
    assert empty_category.products == []  # пустой список


def test_total_product_count():
    """Тестируем счетчик товаров"""
    # Сбрасываем счетчики ПЕРЕД созданием категорий
    Category.category_count = 0
    Category.product_count = 0

    first_category = Category(
        "Одежда",
        "Модная одежда",
        [
            Product("Футболка", "Хлопковая футболка", 99.99, 10),
            Product("Джинсы", "Синие джинсы", 149.99, 15)
        ]
    )

    second_category = Category(
        "Книги",
        "Книги и учебники",
        [
            Product("Учебник", "Учебная литература", 50.99, 5),
            Product("Научная фантастика", "Фантастика", 70.99, 10),
            Product("Книга", "Художественная литература", 69.99, 7)
        ]
    )


    assert Category.category_count == 2
    assert Category.product_count == 5