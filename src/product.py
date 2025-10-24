class Product:
    """Класс для представления товара"""

    def __init__(self, name:str, description:str, price:float, quantity:int):

        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

if __name__ == "__main__":
    product = Product("Футболка", "Хлопковая футболка", 99.0, 10)
    print(product.name)
    print(product.description)
    print(product.price)
    print(product.quantity)
