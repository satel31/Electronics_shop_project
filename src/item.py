import csv
from src.exception_class import InstantiateCSVError


class Item:
    """
    Класс для представления товара в магазине.
    """
    CSV_FILE = "../src/items.csv"
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity

        Item.all.append(self)

    @property
    def name(self) -> str:
        """:returns: Актуальное наименование товара"""
        return self.__name

    @name.setter
    def name(self, new_name: str) -> None:
        """Задаёт новое наименование товара"""
        if len(new_name) <= 10:
            self.__name = new_name
        else:
            raise Exception("Длина наименования товара превышает 10 символов")

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        total_price = self.price * self.quantity
        return total_price

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @classmethod
    def instantiate_from_csv(cls) -> None:
        """Инициализирует экземпляры класса Item данными из файла src/items.csv"""
        try:
            with open(cls.CSV_FILE, encoding='windows-1251') as file:
                file_dict = csv.DictReader(file, delimiter=',')
                for line in file_dict:
                    if len(line) != 3:
                        raise InstantiateCSVError('Файл item.csv поврежден')
                    elif '' in line.keys() or '' in line.values():
                        raise InstantiateCSVError('Файл item.csv поврежден')
                    else:
                        Item(line['name'], line['price'], line['quantity'])
        except FileNotFoundError:
            print('Отсутствует файл item.csv')
        except InstantiateCSVError:
            print('Файл item.csv поврежден')

    @staticmethod
    def string_to_number(value: str) -> int:
        """Преобразует число типа str в int"""
        if '.' in value:
            s = value.split('.')
            return int(s[0])
        else:
            return int(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

    def __str__(self) -> str:
        return f"{self.name}"
