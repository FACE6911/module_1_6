my_dict = {'Иванов': 5, 'Сидоров': 4, 'Шпеньков': 3, 'Смирнов': 5}
print(my_dict)
print(my_dict.get('Иванов'))
print(my_dict.get('Кириллов'))
my_dict.update({'Макров': 4, 'Угальде': 3})
x = my_dict.pop('Сидоров')
print(x)
print(my_dict)

my_set = {1, 2, 'POP', 7, 1, 'POP', 1.2, 6, 10, 1.2}
print(my_set)
my_set.add(28)
my_set.add('GDE')
my_set.remove(2)
print(my_set)

