from src.item import Item

class Phone(Item):
    """
    Класс для представления товара типа телефон в магазине.
    """
    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int) -> None:
        """
        Создание экземпляра класса phone, родительский класс item.
        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        :param number_of_sim: количество поддерживаемых сим-карт
        """
        super().__init__(name, price, quantity)
        self.__number_of_sim = number_of_sim

    @property
    def number_of_sim(self) -> str:
        """:returns: количество поддерживаемых сим-карт"""
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, new_number: int) -> None:
        """Задаёт новое количество поддерживаемых сим-карт"""
        if isinstance(new_number, int) and new_number > 0:
            self.__number_of_sim = new_number
        else:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")

    def __add__(self, other: Item) -> int | str:
        """Cложение по количеству товара в магазине классов Phone и Item"""
        if isinstance(other, Item):
            return self.quantity + other.quantity
        else:
            return f'Складывать можно только экземпляры Phone и Item'

    def __radd__(self, other:Item) -> int | str:
        """Cложение по количеству товара в магазине классов Item и Phone"""
        if isinstance(other, Item):
            return other.quantity + self.quantity
        else:
            return f'Складывать можно только экземпляры Phone и Item'

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.__number_of_sim})"
