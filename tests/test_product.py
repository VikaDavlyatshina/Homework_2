from src.product import Product


"""Тесты для класса Product"""
def test_product_init(product):
    assert product.name == "Футболка"
    assert product.description == "Хлопковая футболка"
    assert product.price == 99.99
    assert product.quantity == 10

def test_product_attributes():
    book = Product("Книга", "Интересная книга", 129.99, 15)

    assert book.name == "Книга"
    assert book.description == "Интересная книга"
    assert book.price == 129.99
    assert book.quantity == 15
