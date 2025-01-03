class House:
    def __init__(self, name, number_of_the_floors):
        self.name = name
        self.number_of_the_floors = number_of_the_floors

    def go_to(self, new_floor):
        if 1 <= new_floor <= self.number_of_the_floors:
            print(f'Вы находитесь в здании {self.name}. Переход на этаж {new_floor}')
            for floor in range(1, new_floor + 1):
                print(floor)
        else:
            print(f'Такого этажа не существует')

    def __len__(self):
        return self.number_of_the_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_the_floors}'

    def __eq__(self, other):
        """Проверить, имеют ли два дома одинаковое количество этажей."""
        if isinstance(other, House):
            return self.number_of_the_floors == other.number_of_the_floors
        return NotImplemented

    def __ne__(self, other):
        """Проверить, имеют ли два дома разное количество этажей."""
        return not self.__eq__(other)

    def __lt__(self, other):
        """Проверить, меньше ли количество этажей в этом доме, чем в другом."""
        if isinstance(other, House):
            return self.number_of_the_floors < other.number_of_the_floors
        return NotImplemented

    def __le__(self, other):
        """Проверить, меньше или равно ли количество этажей в этом доме, чем в другом."""
        if isinstance(other, House):
            return self.number_of_the_floors <= other.number_of_the_floors
        return NotImplemented

    def __gt__(self, other):
        """Проверить, больше ли количество этажей в этом доме, чем в другом."""
        if isinstance(other, House):
            return self.number_of_the_floors > other.number_of_the_floors
        return NotImplemented

    def __ge__(self, other):
        """Проверить, больше или равно ли количество этажей в этом доме, чем в другом."""
        if isinstance(other, House):
            return self.number_of_the_floors >= other.number_of_the_floors
        return NotImplemented

    def __add__(self, value):
        """Увеличить количество этажей на переданное значение value."""
        if isinstance(value, (int, float)):
            self.number_of_the_floors += value
            return self
        return NotImplemented

    def __radd__(self, value):
        """Работает так же, как __add__."""
        return self.__add__(value)

    def __iadd__(self, value):
        """Работает так же, как __add__, но возвращает сам объект."""
        return self.__add__(value)


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)


print(h1)
print(h2)

print(h1 == h2) # __eq__
h1 = h1 + 10 # __add__
print(h1)
print(h1 == h2)
h1 += 10 # __iadd__
print(h1)
h2 = 10 + h2 # __radd__
print(h2)
print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__














