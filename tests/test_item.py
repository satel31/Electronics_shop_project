import pytest
from src.item import Item


@pytest.fixture
def laptop():
    return Item("Ноутбук", 20000, 5)

def test_item_init(laptop):
    """Test of initialization of the class Item"""
    assert laptop.name == "Ноутбук"
    assert laptop.price == 20000
    assert laptop.quantity == 5
    assert len(Item.all) == 1

def test_item_calculate_total_price(laptop):
    """Test of the method calculate_total_price"""
    assert laptop.calculate_total_price() == 100000

def test_item_apply_discount(laptop):
    """"Test of the method apply_discount"""
    laptop.apply_discount()
    assert laptop.price == 20000

def test_item_name(laptop):
    """Test of the method name"""
    assert laptop.name == 'Ноутбук'

def test_item_name_more_than_ten(laptop):
    """Test of the item name with length greater than 10 signs"""
    try:
        Item.name == "СуперСмартфон"
    except Exception:
        pytest.fail("Длина наименования товара превышает 10 символов")
def test_item_name_more_than_ten(laptop):
    Item.name = 'Смартфон'
    assert Item.name == 'Смартфон'
def test_item_instantiate_from_csv():
    """Test  of the method instantiate_from_csv"""
    Item.instantiate_from_csv()
    assert len(Item.all) == 10

def test_item_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5


