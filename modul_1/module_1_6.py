# Работа со словарями
my_dict = {'Имя': 'Панда', 'Год рождения': 1997}
print('Инфо по зверю:', my_dict)
print('Обнаруженный зверь:', my_dict.get('Имя'))
print('Есть у панды хобот:', my_dict.get('Хобот'), 'нет у панды хобота')
my_dict.update({'Фамилия': 'Барсукова',
                'Отчество': 'Муравьедовна',
                'Родилась в городе': 'Зоопарково'})
my_dict.pop('Родилась в городе')
print('Новые данные по зверю:', my_dict)
# Работа с множествами
my_set = {1, 2, 3, 4, 5, 1, 2, 3, 4, 5, True, 'Name', False, 'Name'}
print('Set:', my_set)
my_set.add(11)
my_set.add(20)
my_set.remove(False)
print('Modified set:', my_set)
