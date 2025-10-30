from src.category import Category
from src.utils import create_objects_from_json, read_json


def test_read_json_file_exists():
    """Тест чтения существующего JSON файла"""
    # Предполагаем что файл существует
    data = read_json("../data/products.json")

    assert isinstance(data, list)  # данные должны быть списком
    if data:
        assert len(data) > 0, "Список не должен быть пустым"
        assert "name" in data[0], "У категории должно быть поле name"
        assert "products" in data[0], "У категории должно быть поле products"


def test_create_objects_from_json():
    """Тест создания объектов из JSON данных"""
    # Тестовые данные
    test_data = [
        {
            "name": "Тестовая категория",
            "description": "Тестовое описание",
            "products": [{"name": "Тестовый товар", "description": "Тест", "price": 1000, "quantity": 5}],
        }
    ]

    Category.category_count = 0
    Category.product_count = 0

    categories = create_objects_from_json(test_data)
    products_output = categories[0].products

    assert len(categories) == 1
    assert isinstance(categories[0], Category)
    assert categories[0].name == "Тестовая категория"
    # Проверяем что в строке есть информация о товаре
    assert "Тестовый товар" in products_output
    assert "1000" in products_output
    assert "5 шт." in products_output

def test_create_objects_from_json_empty_products():
    """Тест создания категории с пустым списком товаров"""
    test_data = [
        {
            "name": "Пустая категория",
            "description": "Без товаров",
            "products": []  # Пустой список товаров
        }
    ]

    categories = create_objects_from_json(test_data)

    assert len(categories) == 1
    assert categories[0].name == "Пустая категория"
    assert categories[0].products == "В этой категории пока нет товаров"


