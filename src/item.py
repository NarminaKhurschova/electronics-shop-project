import csv


class Item:
    """
    Класс для представления товара в магазине.
    """
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
        self.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f'{self.__name}'

    @classmethod
    def instantiate_from_csv(cls, path):
        with open(path, 'r', encoding='cp1251') as file:
            cls.all.clear()
            read_file = csv.DictReader(file)
            for row in read_file:
                if None not in row.values():
                    cls(*row.values())
                else:
                    print(f'Проверьте наличие данных о товаре {row["name"]}')
                    continue

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, ch_name):
        if len(ch_name) >= 10:
            self.__name = ch_name[0:10]
        else:
            self.__name = ch_name

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    @staticmethod
    def string_to_number(num):
        return int(float(num))

    def apply_discount(self) -> float:
        """
        Применяет установленную скидку для конкретного товара.
        """

        return self.price * self.pay_rate

