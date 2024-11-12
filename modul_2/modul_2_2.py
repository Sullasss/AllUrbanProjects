first = int(input('Введите число '))
second = int(input('Введите число '))
third = int(input('Введите число '))
if first == second and second == third:
    print('Все', 3, 'числа равны')
elif first == second or first == third or first == third:
    print('равны между собой', 2)
else:
    print(0, 'Нет равных чисел')