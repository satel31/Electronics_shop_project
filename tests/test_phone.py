import pytest
from src.phone import Phone
from src.item import Item

@pytest.fixture
def iphone():
    return Phone("iPhone 14", 120_000, 5, 2)

def test_phone_init(iphone):
    """Test of initialization of the class Phone"""
    assert iphone.name == "iPhone 14"
    assert iphone.price == 120_000
    assert iphone.quantity == 5
    assert iphone.number_of_sim == 2
    assert len(Phone.all) == 1

def test_phone_name(iphone):
    """Test of the method name"""
    assert iphone.number_of_sim == 2

def test_phone_new_number_of_sim():
    """Test of the change of the number_of_sim"""
    phone = Phone("iPhone", 120_000, 5, 2)
    phone.number_of_sim = 3
    assert phone.number_of_sim == 3

def test_phone_new_number_of_sim_zero(iphone):
    """Test of the change of the number_of_sim to zero"""
    try:
        iphone.number_of_sim = 0
    except ValueError:
        pytest.xfail("Количество физических SIM-карт должно быть целым числом больше нуля")

def test_phone_add(iphone):
    """Test of the addition Phone and Item"""
    item1 = Item("Смартфон", 10000, 20)
    assert iphone + item1 == 25

def test_phone_add_bad(iphone):
    """Test of the addition Phone and int"""
    assert iphone + 10_000 == 'Складывать можно только экземпляры Phone и Item'

def test_phone_radd(iphone):
    """Test of the addition Item and Iphone"""
    item1 = Item("Смартфон", 10000, 20)
    assert item1 + iphone == 25

def test_phone_radd_bad(iphone):
    """Test of the addition Phone and int"""
    assert 10_000 + iphone == 'Складывать можно только экземпляры Phone и Item'

def test_repr(iphone):
    """Test if the __repr__ method"""
    assert repr(iphone) == "Phone('iPhone 14', 120000, 5, 2)"
