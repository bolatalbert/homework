# ------ задача 1 ---
# --- надо разобраться как строки 4-6 сделать одной единственной строкой, чтобы не было ошибки: TypeError: write() takes exactly one argument (3 given)
task_1 = open("lesson_5_task_1.txt", "w", encoding="utf-8")
task_1.writelines(input("Введите Ваше имя\n"))
task_1.writelines(input("Введите фамилию\n"))
task_1.writelines(input("Сколько Вам лет?\n"))

task_1.close()
task_1_print = open("lesson_5_task_1.txt", "r", encoding="utf-8")
print(f"file with name lesson_5_task_1.txt was created\n", task_1_print.read())
task_1_print.close()
