from src.product import Product
from typing import Optional, List, Union, Any



class Category:
    """Класс для представления категорий товаров"""

    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: Optional[List[Product]] = None):
        self.name = name
        self.description = description
        self.__products = products if products is not None else []
        Category.category_count += 1

        for product in self.__products:
            if isinstance(product, Product):
                Category.product_count += 1
            else:
                self.__products.remove(product)

    def __str__(self):
        """Магический метод для строкового представления категории"""
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    def add_product(self, product: Union[Product, Any]):
        """Добавляет товар в категорию"""
        # Проверяем, что product является подклассом Product
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только объекты класса Product и его наследников!")
        self.__products.append(product)
        Category.product_count += 1
        print(f"Товар '{product.name}' добавлен в категорию '{self.name}'")


    @property
    def products(self):
        """Геттер для вывода товаров в нужном формате"""
        if not self.__products:
            return "В этой категории пока нет товаров"

        product_list = [str(product) for product in self.__products]
        return "\n".join(product_list)


if __name__ == "__main__":  # pragma: no cover
    product1 = Product("Футболка", "Хлопковая футболка", 99.99, 10)
    product2 = Product("Джинсы", "Синие джинсы", 149.99, 15)

    clothes = Category("Одежда", "Модная одежда", [product1, product2])

    print("Товары категории")
    print(clothes.products)

    print(f"\nВсего категорий: {Category.category_count}")
    print(f"\nВсего товаров: {Category.product_count}")
