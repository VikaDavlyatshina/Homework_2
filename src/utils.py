import json
import os
from typing import List

from src.category import Category
from src.product import Product


def read_json(path: str) -> List[dict]:
    try:
        full_path = os.path.abspath(path)
        with open(full_path, "r", encoding="UTF-8") as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print(f"Ошибка: файл {path} не найден")
        return []
    except json.JSONDecodeError:
        print(f"Ошибка: файл {path} содержит некорректный JSON!")
        return []
    except Exception as e:
        print(f"Неожиданная ошибка при чтении файла {path}: {e}")
        return []


def create_objects_from_json(data: List[dict]) -> List[Category]:

    categories_list: List[Category] = []

    if not data:
        print("Нет данных для создания объектов")
        return categories_list

    for category_data in data:
        try:
            products_list: List[Product] = []

            products_data = category_data.get("products", [])

            for product_data in products_data:
                try:
                    product = Product.new_product(product_data, products_list)
                    products_list.append(product)
                    print(f"Создан товар {product.name}")
                except Exception as e:
                    print(f"Ошибка при создании товара: {e}")

            # Создаем категорию, исключая поле "products" из словаря
            category_args = {
                "name": category_data["name"],
                "description": category_data["description"],
                "products": products_list,
            }
            category = Category(**category_args)
            categories_list.append(category)
            print(f"Создана категория: {category.name} с {len(products_list)} товарами")

        except KeyError as e:
            print(f"Ошибка: в данных категории отсутствует обязательное поле {e}")
        except Exception as e:
            print(f"Ошибка при создании категории {e}")

    return categories_list
