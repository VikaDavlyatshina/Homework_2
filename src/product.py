from typing import List, Optional
from abc import ABC, abstractmethod

class BaseProduct(ABC):
    """Абстрактный базовый класс для всех продуктов"""

    @abstractmethod
    def __init__(self, name: str, description: str, price: float, quantity: int):
        """Абстрактный конструктор.

        Args:
            name: Название продукта
            description: Описание продукта
            price: Цена продукта
            quantity: Количество на складе
        """
        pass

    @abstractmethod
    def __str__(self) -> str:
        """Абстрактный метод для строкового представления"""
        pass

    @abstractmethod
    def get_additional_info(self) -> dict:
        """Абстрактный метод для получения дополнительной информации"""
        pass

class ReprMixin:
    """Миксин для строкового представления"""
    def __repr__(self) -> str:
        class_name = self.__class__.__name__
        attributes = []
        for value in self.__dict__.values():
            if isinstance(value, str):
                attributes.append(f"'{value}'")
            else:
                attributes.append(str(value))
        return f"{class_name}({', '.join(attributes)})"


class Product(ReprMixin, BaseProduct):
    """Класс для представления товара"""

    def __init__(self, name: str, description: str, price: float, quantity: int):

        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __str__(self):
        """Магический метод для строкового представления товара"""
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def get_additional_info(self) -> dict:
        """Возвращает дополнительную информацию о продукте"""
        return {
            "type": "Базовый продукт",
            "category": "Общая категория"
        }

    def __add__(self, other):
        """Магический метод, который возвращает общую стоимость всех товаров на складе"""
        if type(self) is not type(other):
            raise TypeError("Можно складывать только товары из одинаковых классов продуктов")
        return (self.price * self.quantity) + (other.price * other.quantity)

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
            if answer.lower() not in ["y", "yes"]:
                print("Изменение цены отменено")
                return

        self.__price = new_price

    @classmethod
    def new_product(cls, product_data: dict, product_list: Optional[List["Product"]] = None):
        """Создает товар из словаря с проверкой дубликатов"""
        # Если передан список товаров - ищем дубликаты
        if product_list:
            for existing_product in product_list:
                # Проверяем похожие названия
                if existing_product.name.lower() == product_data["name"].lower():
                    print(f"Найден дубликат {existing_product.name}")
                    return cls(
                        name=existing_product.name,
                        description=existing_product.description,
                        # Выбираем большую цену
                        price=max(existing_product.price, product_data["price"]),
                        # Складываем количество
                        quantity=existing_product.quantity + product_data["quantity"],
                    )

        return cls(
            name=product_data["name"],
            description=product_data["description"],
            price=product_data["price"],
            quantity=product_data["quantity"],
        )


class Smartphone(Product):
    """Класс для Смартфонов - наследуется от Product"""

    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency  # производительность
        self.model = model  # модель
        self.memory = memory  # объём памяти
        self.color = color  # цвет

    def __str__(self):
        """Переопределяем строковое представление для смартфона"""
        base_info = super().__str__()  # берём базовую информацию
        return (
            f"{base_info}\n"
            f"Производительность: {self.efficiency}, "
            f"Модель: {self.model}, "
            f"Память: {self.memory} ГБ, "
            f"Цвет: {self.color}"
        )

    def get_additional_info(self) -> dict:
        """Возвращает дополнительную информацию о смартфоне"""
        return {
            "type": "Смартфон",
            "performance": self.efficiency,
            "model": self.model,
            "memory_gb": self.memory,
            "color": self.color
        }


class LawnGrass(Product):
    """Класс Трава газонная - наследуется от Product"""

    def __init__(self, name, description, price, quantity, country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country  # страна-производитель
        self.germination_period = germination_period  # срок прорастания
        self.color = color  # цвет

    def __str__(self):
        """Переопределяем строковое представление для смартфона"""
        base_info = super().__str__()  # берём базовую информацию
        return (
            f"{base_info}\n"
            f"Страна-производитель: {self.country}, "
            f"Срок прорастания: {self.germination_period}, "
            f"Цвет: {self.color}"
        )

    def get_additional_info(self) -> dict:
        """Возвращает дополнительную информацию о газонной траве"""
        return {
            "type": "Газонная трава",
            "country": self.country,
            "germination_period": self.germination_period,
            "color": self.color
        }
