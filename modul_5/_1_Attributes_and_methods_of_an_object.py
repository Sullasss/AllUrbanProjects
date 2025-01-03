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


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)

h1.go_to(5)
h2.go_to(10)
