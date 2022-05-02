# Альберт, задание 1
name = input("Введите Ваше имя: ")
age = int(input("Сколько Вам лет: "))
country = input("Из какой Вы страны: ")
pet = input("Имя домашнего животного: ")
print(f"Вас зовут: {name} , Вам {age} лет, Вы из {country} и у Вас есть животное по имени {pet}")

# задание 2 -- про часы

time = int(input("Введите время в секундах (введите целое число): "))
if time <= 59:
    print (f"00:00:{time}")
elif time >= 60 and time <= 3600:
    print (f"00:{time // 60}:{(time - (time // 60) * 60)}")
elif time >= 3600:
    print (f"{time // 3600}:{(time % 3600) // 60}:{(time - (time // 60) * 60)}")


# задание 3
n = int(input('введите целое число n: '))
nn = (f"{n}{n}")
nnn = (f"{n}{n}{n}")
print (f"{n} + {nn} + {nnn} = ", int(n) + int(nn) + int(nnn))

# задание 4 -- решил не самостоятельно

number = int(input("введите целое положительное число:"))
y = number % 10
while number >= 1:
    number = number // 10
    if number % 10 > y:
        y = number % 10
    if number > 9:
        continue
    else:
        print(f"наибольшая цифра равна {y}")
        break

# задание 5

income = int(input("Введите выручку -- целое число: "))
costs = int(input("Введите издержки -- целое числе: "))
if income > costs:
    print("Фирма в плюсе -- капуста рубится -- надо бы рассчитать рентабельность!")
    profit = int(input("Введите Вашу чистую прибыль -- целое число: "))
    print ("Рентабельность = ", (profit / income) * 100 , "% и давайте рассчитаем прибыль на 1 сотрудника")
    workers = int(input("Введите число сотрудников:" ))
    print ("Прибыль на одного сотрудника = ", profit / workers )
else:
    print("Фирма в минусе -- левеха не мутится))")

# задание 6 -- нужно научиться округлять результат!!!

a = int(input("Введите результат в первый день -- км: "))
b = int(input("Введите конечную цель -- км в день: "))
target = a
while a <= b:
    a = a + ((a / 100) * 10)
    if a >= b:
        i = (a - target) / ((target / 100) * 10)
        print(f"Вы без сомнений достигнете цели в {a} км через {i} дней")

# конец

