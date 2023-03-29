import pytest
from src.keyboard import KeyBoard, MixinKL

@pytest.fixture
def keyboard():
    return KeyBoard('Dark Project KD87A', 9600, 5)

def test_keyboard_init(keyboard):
    """Test of initialization of the class KeyBoard"""
    assert keyboard.name == "Dark Project KD87A"
    assert keyboard.price == 9600
    assert keyboard.quantity == 5
    assert keyboard._language == "EN"
    assert len(KeyBoard.all) == 1

def test_keyboard_language(keyboard):
    """Test of the property function language of the class KeyBoard"""
    assert keyboard.language == "EN"

def test_mixinkl_init():
    """Test of initialization of the class MixinKL"""
    test_mixinkl = MixinKL()
    assert test_mixinkl._language == "EN"

def test_mixinkl_change_lang(keyboard):
    keyboard.change_lang()
    assert str(keyboard.language) == "RU"
    keyboard.change_lang().change_lang()
    assert str(keyboard.language) == "RU"
