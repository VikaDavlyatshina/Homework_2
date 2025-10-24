from src.utils import read_json, create_objects_from_json
from src.category import Category
from src.product import Product


def test_read_json_file_exists():
    """Тест чтения существующего JSON файла"""
    # Предполагаем что файл существует
    data = read_json("data/products.json")

    assert isinstance(data, list)  # данные должны быть списком
    assert len(data) > 0  # список не пустой


def test_create_objects_from_json():
    """Тест создания объектов из JSON данных"""
    # Тестовые данные
    test_data = [
        {
            "name": "Тестовая категория",
            "description": "Тестовое описание",
            "products": [
                {
                    "name": "Тестовый товар",
                    "description": "Тест",
                    "price": 1000,
                    "quantity": 5
                }
            ]
        }
    ]

    categories = create_objects_from_json(test_data)

    assert len(categories) == 1
    assert isinstance(categories[0], Category)
    assert categories[0].name == "Тестовая категория"
    assert len(categories[0].products) == 1
    assert isinstance(categories[0].products[0], Product)
    assert categories[0].products[0].name == "Тестовый товар"