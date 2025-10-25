from typing import Optional, List, Any


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
            answer = input(f"Цена понижается с {self.__price} до {new_price}." f" Подтвердите выбор (y/n): ")
            if answer.lower() not in ["y", "yes"]:
                print("Изменение цены отменено")
                return

        self.__price = new_price

    @classmethod
    def new_product(cls, product_data: dict, product_list: Optional[List[Any]] = None):
        """Создает товар из словаря с проверкой дубликатов"""
        # Если передан список товаров - ищем дубликаты
        if product_list:
            for existing_product in product_list:
                # Проверяем похожие названия
                if existing_product.name.lower() == product_data["name"].lower():
                    print(f"Найден дубликат: {existing_product.name}")

                    # Складываем количество
                    total_quantity = existing_product.quantity + product_data["quantity"]

                    # Выбираем большую цену
                    highest_price = max(existing_product.price, product_data["price"])

                    # Обновляем существующий
                    existing_product.quantity = total_quantity
                    existing_product.price = highest_price

                    print(f"Объединено: количество = {total_quantity}, цена = {highest_price}")
                    return existing_product

        return cls(
            name=product_data["name"],
            description=product_data["description"],
            price=product_data["price"],
            quantity=product_data["quantity"],
        )
