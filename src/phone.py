from src.item import Item

class Phone(Item):
    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int):
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
            self.__new_number = new_number
        else:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")

    def __add__(self, other):
        if isinstance(other, Item):
            return self.quantity + other.quantity

    def __radd__(self, other):
        if isinstance(other, Item):
            return other.quantity + self.quantity

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.__number_of_sim})"
