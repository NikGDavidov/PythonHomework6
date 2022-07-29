# Найти сумму чисел списка стоящих на нечетной позиции


list1 = [int(i) for i in input().split()]  # заполняем список

# res = sum(list[::2]) # так проще всего

# с использованием лямбд, filter, map, enumerate
en = enumerate(list1)
# print(en)
res = list(filter(lambda x:x[0]%2 == 0, en)) #предполагаем что позиция 1 - нечетная, соответствует индексу 0 (четному)
res = list(map(lambda x:x[1], res ))
result = sum(res)

print (f'{list1} -> {result}')