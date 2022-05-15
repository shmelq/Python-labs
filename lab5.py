list1 = input("Введите список слов через запятую:")
list1 = set(list1.split(','))  # split сканирует строку и разделяет ее в случае нахождения разделителя
print(list1)
count_list1 = len(list1)
print("Слов в списке:", count_list1)  #количество слов в списке
list2 = input(" Введите второй список с таким же количеством символов через запятую: ")
list2 = set(list2.split(','))
if (len(list2)) != (len(list1)):
    print('Вы ввели не такое же количество слов')
    exit()
else:
    slovar = dict(zip(list1, list2))  #создание словаря
print(slovar)
