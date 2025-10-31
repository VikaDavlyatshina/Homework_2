from src.category import Category
from src.utils import create_objects_from_json, read_json


def test_read_json_file_exists(create_test_json_file):
    """Тест чтения существующего JSON файла"""
    # Предполагаем что файл существует
    data = read_json(create_test_json_file)

    assert isinstance(data, list)  # данные должны быть списком
    assert len(data) > 0, "Список не должен быть пустым"
    assert "name" in data[0], "У категории должно быть поле name"
    assert "products" in data[0], "У категории должно быть поле products"


def test_create_objects_from_json(valid_json_data):
    """Тест создания объектов из JSON данных"""

    Category.category_count = 0
    Category.product_count = 0

    categories = create_objects_from_json(valid_json_data)
    products_output = categories[0].products

    assert len(categories) == 1
    assert isinstance(categories[0], Category)
    assert categories[0].name == "Одежда"
    # Проверяем что в строке есть информация о товаре
    assert "Футболка" in products_output
    assert "99.99" in products_output
    assert "10 шт." in products_output


def test_read_json_file_not_exist(capsys):
    """Тест для чтения несуществующего файла"""
    data = read_json("non_existent_file.json")

    assert data == []
    # Проверяем сообщение об ошибке
    captured = capsys.readouterr()
    assert "не найден" in captured.out


def test_create_objects_from_empty_data(empty_data):
    """Тест создания объектов из пустых данных"""
    categories = create_objects_from_json(empty_data)
    assert categories == []


def test_create_objects_with_missing_fields(json_data_with_missing_fields, capsys):
    """Тест с данными, где отсутствуют обязательные поля"""
    categories = create_objects_from_json(json_data_with_missing_fields)
    assert len(categories) == 0

    captured = capsys.readouterr()
    assert "отсутствует обязательное поле" in captured.out


def test_read_json_empty_file(create_empty_json_file, capsys):
    """Тест для чтения пустого Json файла"""
    data = read_json(create_empty_json_file)

    assert data == []
    captured = capsys.readouterr()
    assert "Ошибка" not in captured.out


def test_read_json_invalid_file(create_invalid_json_file, capsys):
    """Тест чтения файла с некорректным JSON"""
    data = read_json(create_invalid_json_file)

    assert data == []
    captured = capsys.readouterr()
    assert "содержит некорректный JSON" in captured.out


def test_create_objects_multiple_categories(create_test_json_file):
    """Тест создания нескольких категорий"""
    # Читаем данные из фикстуры
    test_data = read_json(create_test_json_file)

    # Добавляем вторую категорию
    test_data.append(
        {
            "name": "Электроника",
            "description": "Техника",
            "products": [{"name": "Смартфон", "description": "Телефон", "price": 50000, "quantity": 3}],
        }
    )

    categories = create_objects_from_json(test_data)

    assert len(categories) == 2
    assert categories[0].name == "Одежда"
    assert categories[1].name == "Электроника"
