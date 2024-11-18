# Определим входные данные
my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]  # исходный список
count = 0   # задаём счетчик
print('Список', my_list, '\nПоложительные числа из списка')
while count < len(my_list):
    num = my_list[count]  # задаём число из списка (Для того что бы обратиться к списку через новую переменную)
    count = count + 1 # запускаем счетчик
    if num == 0: # прописываем условие внутри цикла, что бы пропустить 0
        continue # пропускаем 0
    elif num < 0:
        print('Встретилось отрицательное число:', num)
        break
    elif count == len(my_list):
        print(num)
        print('Список закончился')
    else:
        print(num)
# решение преподавателя
# my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
# index_elem = 0
# while index_elem < len(my_list):
#     elem = my_list[index_elem]
#     index_elem += 1
#     if elem == 0:
#         continue
#     elif elem < 0:
#         break
#     else:
#         print(elem)