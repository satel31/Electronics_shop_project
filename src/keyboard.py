from src.item import Item

class MixinKL:
    """Дополнительный функционал по хранению и изменению раскладки клавиатуры"""
    def __init__(self):
        self.language = 'EN'

    def change_lang(self) -> MixinKL:
        """Меняет раскладку клавиатуры
           Возвращает self с новой раскладкой (для прохождения теста kb.change_lang().change_lang())"""
        if self.language == 'EN':
            self.language = 'RU'
        elif self.language == 'RU':
            self.language = 'EN'
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
        self.language = 'EN'


