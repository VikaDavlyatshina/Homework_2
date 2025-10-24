from src.product import Product

class Category:
    """Класс для представления категорий товаров"""

    total_categories = 0
    total_products = 0

    def __init__(self, name:str, description:str, products:list):
        self.name = name
        self.description = description
        self.products = products if products is not None else []

        Category.total_categories += 1
        Category.total_products += len(self.products)


if __name__ == "__main__":
    product1 = Product("Футболка", "Хлопковая футболка", 99.99, 10)
    product2 = Product("Джинсы", "Синие джинсы", 149.99, 15)

    clothes = Category("Одежда", "Модная одежда", [product1, product2])

    print("Товары категории")
    for product in clothes.products:
        print(f"-{product.name} - {product.price} руб")

    print(f"\nВсего категорий: {Category.total_categories}")
    print(f"\nВсего товаров: {Category.total_products}")