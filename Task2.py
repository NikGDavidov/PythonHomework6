# 2) Задача: предложить улучшения кода для уже решённых задач с помощью использования **лямбд, filter, map, zip, enumerate, list comprehension

# Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.
# Пример:

# [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]

# list1 = [1, 2, 3, 5, 1, 5, 3, 10]
list1 = [int(i) for i in input().split()]  #заполняем список 
# [listUnic.append(i) for i in list1 if  list1.count(i)==1] #можно и так
listUnic = list(filter(lambda x:list1.count(x)==1, list1)) # записываем уникальные элементы через filter
print(f'{list1} -> {listUnic}')
