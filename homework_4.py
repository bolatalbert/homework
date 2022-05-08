# задача 1 -- запускается через скрипт, при запуске файла
# команда в терминале: python homework_4.py a b c -- где a b c -- значения через пробел
from sys import argv

script_name, hours, cash_per_hour, extra_cash = argv

print ("Имя скрипта: ", script_name)
print("Отработано часов: ", hours)
print("Ставка в час: ", cash_per_hour)
print("Премия: ", extra_cash)
a = float(hours)
b = float(cash_per_hour)
c = float(extra_cash)
print("Заработная плата: ", (a * b) + c)




# Задача 2
my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = [my_list[index] for index in range(1, len(my_list)) if my_list[index] > my_list[index - 1]]
print(new_list)

#Задача 3
list_20_21 = [el for el in range(20, 241) if el % 20 == 0 or el % 21 ==0]
print(list_20_21)

#Задача 4
from random import randint

my_list_new = [randint(-10, 10) for _ in range(20)]
uniq_list = [el for el in my_list_new if my_list_new.count(el) == 1]
print(f"Source list\n{my_list_new}\nNo repetition list\n{uniq_list}")

# Задача 5

from functools import reduce

def list_mul(n_1, n_2):
    return n_1 * n_2

list_mul_result = [el for el in range(100, 1001, 2)]
print(reduce(list_mul, list_mul_result))



# Задача 6-1
from itertools import count
for el in count(3):
    if el > 10:
        break
    else:
        print(el)

from itertools import count
from math import factorial

def fact_gen():
    for el in count(1):
        yield factorial(el)

x = 0
for i in fact_gen():
    if x == 15:
        break
    else:
        x = x + 1
        print("Факториал числа", x, "равен", i)


