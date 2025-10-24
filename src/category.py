from src.product import Product


class Category:
    """Класс для представления категорий товаров"""

    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list):
        self.name = name
        self.description = description
        self.products = products if products is not None else []

        Category.category_count += 1
        Category.product_count += len(self.products)


if __name__ == "__main__":  # pragma: no cover
    product1 = Product("Футболка", "Хлопковая футболка", 99.99, 10)
    product2 = Product("Джинсы", "Синие джинсы", 149.99, 15)

    clothes = Category("Одежда", "Модная одежда", [product1, product2])

    print("Товары категории")
    for product in clothes.products:
        print(f"-{product.name} - {product.price} руб")

    print(f"\nВсего категорий: {Category.category_count}")
    print(f"\nВсего товаров: {Category.product_count}")
