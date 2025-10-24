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

def test_price_setter_negative(product, capsys):
    product.price = -50
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out
    assert product.price == 99.99

def test_price_setter_zero(product, capsys):
    product.price = 0
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out
    assert product.price == 99.99

def test_new_product_with_duplicates( product_data):
    existing_products = [
        Product("Телефон", "Смартфон", 25000, 8)
        ]

    # Создаем "дубликат" - товар с таким же названием
    new_product = Product.new_product(product_data, existing_products)

    # Должен вернуть существующий товар с обновленными данными
    assert new_product.quantity == 13
    assert new_product.price == 25000 # Более высокая цена