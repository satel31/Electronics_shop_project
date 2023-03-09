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




