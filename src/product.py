class Product:
    """Класс для представления товара"""

    def __init__(self, name: str, description: str, price: float, quantity: int):

        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @property
    def price(self):
        """Геттер для цены"""
        return self.__price

    @price.setter
    def price(self, new_price: float):
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return

        if new_price < self.__price:
            answer = input(f"Цена понижается с {self.__price} до {new_price}. Подтвердите выбор (y/n): ")
            if answer.lower() not in ['y', 'yes']:
                print("Изменение цены отменено")
                return

        self.__price = new_price

    @classmethod
    def new_product(cls, product_data: dict, product_list: list=None):
      """Создает товар из словаря с проверкой дубликатов"""
      # Если передан список товаров - ищем дубликаты
      if product_list:
          for existing_product in product_list:
              # Проверяем похожие названия
              if existing_product.name.lower() == product_data['name'].lower():
                  print(f"Найден дубликат: {existing_product.name}")

                  # Складываем количество
                  total_quantity = existing_product.quantity +product_data['quantity']

                  # Выбираем большую цену
                  highest_price = max(existing_product.price, product_data['price'])

                  # Обновляем существующий
                  existing_product.quantity = total_quantity
                  existing_product.price = highest_price

                  print(f"Объединено: количество = {total_quantity}, цена = {highest_price}")
                  return existing_product


      return cls(
           name=product_data['name'],
           description=product_data['description'],
           price=product_data['price'],
           quantity=product_data['quantity'])


if __name__ == "__main__":
    product1 = Product("Honor", "Смартфон", 20000, 10)
    print(f"Создан товар {product1.name}, цена: {product1.price} руб")

    product1.price = 25000
    print(f"Цена изменена на {product1.price} руб")

    product1.price = -100
    print(f"Цена осталась: {product1.price} (не изменилась)")

    products = {
        "name": "Samsung",
        "description": "Android телефон",
        "price": 40000,
        "quantity": 5
    }
    product2 = Product.new_product(products)
    print(f" Создан через класс-метод: {product2.name}, цена: {product2.price}")

    # Тест 5: Проверяем объединение дубликатов
    product_data_duplicate = {
        "name": "samsung",  # тот же товар в другом регистре
        "description": "Новая модель",
        "price": 45000,  # большая цена
        "quantity": 3  # добавляемое количество
    }

    existing_products = [product2]
    result = Product.new_product(product_data_duplicate, existing_products)
    print(f" Объединённый товар: {result.name}, цена: {result.price}, количество: {result.quantity}")

