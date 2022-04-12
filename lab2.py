name = input("Введите строку: ")
name2 = name[:-1]
name3 = " "
for x in range(0, len(name2)):
    if x == 2:
        continue
    else:
        name3 = name3 + name2[x]
print(name3)
if name.find("с") == 0:
    print("В строке есть 'с'")
