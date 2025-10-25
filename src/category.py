from src.product import Product


class Category:
    """Класс для представления категорий товаров"""

    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list=None):
        self.name = name
        self.description = description
        self.__products = products if products is not None else []
        Category.category_count += 1

        for product in self.__products:
            if isinstance(product, Product):
                Category.product_count += 1


    def __str__(self):
        """Магический метод для строкового представления категории"""
        total_quantity = sum(product.quantity for product in self.__products)
        return  f"{self.name}, количество продуктов: {total_quantity} шт."

    def _get_products(self):
        """Защищенный метод для доступа к товарам"""
        return self.__products

    def __iter__(self):
        """Магический метод для поддержки итерации"""
        return self.ProductIterator(self)

    class ProductIterator:
        """Вспомогательный класс для итерации по товарам категории"""

        def __init__(self, category):
            """
            category - объект класса Category
            """
            self.category = category
            self.index = 0

        def __iter__(self):
            """Возвращает итератор"""
            return self

        def __next__(self):
            """Возвращает следующий товар в категории"""
            products = self.category._get_products()
            if self.index < len(products):
                product = products[self.index]
                self.index += 1
                return product
            else:
                raise StopIteration

    def add_product(self, product: Product):
        """Добавляет товар в категорию"""
        # Проверяем, что передан объект Product
        if isinstance(product, Product):
            if product not in self.__products:
              self.__products.append(product)
              Category.product_count += 1
              print(f"Товар '{product.name}' добавлен в категорию '{self.name}'")
            else:
               print(f"Товар '{product.name}' уже есть в категории")
        else:
            print("Можно добавлять только объекты класса Product!")

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

if __name__ == "__main__":
    # Тестируем ВСЕ функции
    product1 = Product("Футболка", "Хлопковая футболка", 99.99, 10)
    product2 = Product("Джинсы", "Синие джинсы", 149.99, 15)

    print("✅ Строковое представление товара:")
    print(product1)

    print("\n✅ Сложение товаров:")
    total = product1 + product2
    print(f"Общая стоимость: {total} руб.")

    print("\n✅ Создание категории:")
    clothes = Category("Одежда", "Модная одежда", [product1, product2])
    print(clothes)

    print("\n✅ Геттер products:")
    print(clothes.products)

    print("\n✅ Итерация по категории:")
    for product_ in clothes:
        print(f" - {product_}")

    print(f"\n✅ Статистика:")
    print(f"Всего категорий: {Category.category_count}")
    print(f"Всего товаров: {Category.product_count}")

    print("\n✅ Проверка дубликатов:")
    clothes.add_product(product1)
