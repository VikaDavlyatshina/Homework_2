import json
import os

from src.category import Category
from src.product import Product


def read_json(path: str) -> dict:
    full_path = os.path.abspath(path)
    with open(full_path, "r", encoding="UTF-8") as file:
        data = json.load(file)
    return data


def create_objects_from_json(data):
    categories_list = []

    for category_data in data:
        products_list = []

        for product_data in category_data["products"]:
            # Используем ** для распаковки словаря
            product = Product(**product_data)
            products_list.append(product)

        # Создаем категорию, исключая поле "products" из словаря
        category_args = {
            "name": category_data["name"],
            "description": category_data["description"],
            "products": products_list,
        }
        category = Category(**category_args)
        categories_list.append(category)

    return categories_list


if __name__ == "__main__":
    raw_data = read_json("../data/products.json")
    categories = create_objects_from_json(raw_data)

    for category in categories:
        print(f" {category.name} ({len(category.products)} товаров)")

        for product in category.products:
            print(f"{product.name} - {product.price} руб.")
            print(f"остаток: {product.quantity}")
