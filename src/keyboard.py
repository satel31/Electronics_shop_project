from src.item import Item

class MixinKL:
    """Дополнительный функционал по хранению и изменению раскладки клавиатуры"""
    def __init__(self):
        self._language = 'EN'

    def change_lang(self):
        """Меняет раскладку клавиатуры
           Возвращает self с новой раскладкой (для прохождения теста kb.change_lang().change_lang())"""
        if self._language == 'EN':
            self._language = 'RU'
        elif self._language == 'RU':
            self._language = 'EN'
        return self


class KeyBoard(Item, MixinKL):
    """
    Класс для представления товара типа телефон в магазине.
    """
    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса keyboard, родительский класс item.
        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        :param language: язык клавиатуры
        """
        super().__init__(name, price, quantity)
        self._language = 'EN'

    @property
    def language(self):
        return self._language
