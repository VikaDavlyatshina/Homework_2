from src.category import Category
from src.product import Product

"""Тест для класса Category"""

def test_category_init(first_category, second_category):
    """Тест инициализации"""
    assert first_category.name == "Одежда"
    assert first_category.description == "Модная одежда"

    products_str = first_category.products
    assert "Футболка" in products_str
    assert "Джинсы" in products_str
    assert "99.99" in products_str
    assert "149.99" in products_str

def test_category_products_format(first_category):
    products_output = first_category.products

    assert "Футболка, 99.99 руб. Остаток: 10 шт." in products_output
    assert "Джинсы, 149.99 руб. Остаток: 15 шт." in products_output

    lines = products_output.split('\n')
    assert len(lines) == 2

def test_empty_category():
    """Тест: можно создать категорию без товаров"""
    empty_category = Category("Электроника", "Техника", [])

    assert empty_category.name == "Электроника"
    assert empty_category.products == ""


def test_total_product_count():
    """Тестируем счетчик товаров"""
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

def test_add_product_to_category(first_category, capsys):
    new_product = Product("Куртка", "Зимняя куртка", 299.99, 3)

    initial_count = Category.product_count

    first_category.add_product(new_product)

    captured = capsys.readouterr()
    assert "Товар 'Куртка' добавлен в категорию 'Одежда'" in captured.out

    products_output = first_category.products
    assert "Куртка, 299.99 руб. Остаток: 3 шт." in products_output
    assert Category.product_count == initial_count + 1