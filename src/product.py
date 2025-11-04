from abc import ABC, abstractmethod
from typing import List, Optional


class BaseProduct(ABC):
    """Базовый абстрактный класс для всех продуктов"""

    @abstractmethod
    def __init__(self, name: str, description: str, price: float, quantity: int):
        pass

    @abstractmethod
    def __str__(self) -> str:
        """Абстрактный метод для строкового представления"""
        pass


class ReprMixin:
    """Миксин для печати в консоль при создании объекта"""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, *args, **kwargs):
        """Конструктор миксина - печатает в консоль после создания объекта"""
        super().__init__(*args, **kwargs)
        print(repr(self))

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}("{self.name}", "{self.description}", {self.price}, {self.quantity})'


class Product(ReprMixin, BaseProduct):
    """Класс для представления товара"""

    def __init__(self, name: str, description: str, price: float, quantity: int):

        if quantity == 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен.")
        elif quantity < 0:
            raise ValueError("Остаток товара не должен быть отрицательным.")

        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

        super().__init__(name, description, price, quantity)

    def __str__(self):
        """Магический метод для строкового представления товара"""
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

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
        self.efficiency = efficiency  # производительность
        self.model = model  # модель
        self.memory = memory  # объём памяти
        self.color = color  # цвет

        super().__init__(name, description, price, quantity)

    def __repr__(self):
        return (
            f'{self.__class__.__name__}("{self.name}", "{self.description}", {self.price}, {self.quantity}, '
            f'"{self.efficiency}", "{self.model}", {self.memory}, "{self.color}")'
        )

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


class LawnGrass(Product):
    """Класс Трава газонная - наследуется от Product"""

    def __init__(self, name, description, price, quantity, country, germination_period, color):
        self.country = country  # страна-производитель
        self.germination_period = germination_period  # срок прорастания
        self.color = color  # цвет

        super().__init__(name, description, price, quantity)

    def __repr__(self):
        return (
            f'{self.__class__.__name__}("{self.name}", "{self.description}", {self.price}, {self.quantity}, '
            f'"{self.country}", "{self.germination_period}", "{self.color}")'
        )

    def __str__(self):
        """Переопределяем строковое представление для смартфона"""
        base_info = super().__str__()  # берём базовую информацию
        return (
            f"{base_info}\n"
            f"Страна-производитель: {self.country}, "
            f"Срок прорастания: {self.germination_period}, "
            f"Цвет: {self.color}"
        )


product1 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
