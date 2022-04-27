
# задание 1 -- вроде бы добавил ошибку деления на 0 -- но except не срабатывает!

def my_fun (arg_1, arg_2):
    try:
        arg_1, arg_2 = int(arg_1), int(arg_2)
    except ValueError:
        return "Value Error"
    except ZeroDivisionError:
        return "You can't divide by 0"
    return arg_1 / arg_2

print(my_fun(input("Enter first value: "), input("Enter second value: ")))

# задание 2

def my_dict (*args):
    return (args)

print(my_dict(input("Enter name: "), input("last name: "), input("Date of birth: "), input("City: "), input("E-mail: "), input("Phone: ")))

# задание 3

def my_fun_3():
    x = float(input("Enter x: "))
    y = float(input("Enter y: "))
    z = float(input("Enter z: "))
    if x <= y and x <= z:
        return y + z
    elif y <= x and y <= z:
        return x + z
    elif z <= y and z <= x:
        return y + x
result_3 = my_fun_3()
print(result_3)

# задание 4

def my_degree():
    try:
        x = int(input("Enter x: "))
        y = int(input("Enter y: "))
    except y >= 0:
        return
    return x ** y
print(my_degree())

# Задание 5 -- самостоятельно не смог решить. Решил после Вашего объяснения.


# Задание 6

def my_func_Text (*args):
    return (args)
print(my_func_Text(input("Введите слова через пробел").title()))




