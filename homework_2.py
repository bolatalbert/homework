# -------- УРОК 2 -------

# задание 1

list_a = [1000, True, 4444.4, "str-1", 5000]
print(type(list_a[0]), type(list_a[1]), type(list_a[2]), type(list_a[3]), type(list_a[4]))

# задание 2 -- не выполнил пока

a = list(input("Введите элементы в список: "))
new_a = []
temp1 = 0
temp2 = 0
tem = a
for el in a:
    new_a.append(el)
    print(new_a)

# задание 3 -- решение через словарь

months = {1 : "jan",2 : "feb",3: "mar", 4 : "apr", 5 : "may", 6 : "jun", 7 : "jul", 8 : "aug", 9 : "sept", 10 :"oct", 11 : "nov", 12 : "dec"}
a = int(input("Введите месяц от 1 до 12: "))
print(months.get(a))

# задание 3 -- решение через список

months_list = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sept", "oct", "nov", "dec"]
b = int(input("Введите месяц от 1 до 12: "))
if b >= 1 and b <= 12:
    el = b-1
    print(months_list[el])
else:
    print("Вы ввели неверное значение")

# задание 4
str_1 = input("Введите слова через пробел: ")
print(str_1.replace(" ", "\n"))

# задание 5

list_rating = [7, 5, 3, 3, 2]
x = int(input("Введите целое число: "))
list_rating.append(x)
list_rating.sort()
list_rating.reverse()
print(list_rating)


















