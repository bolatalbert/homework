# ----- Задание 2 --- не до конца разобрался как высчитывать число слов в каждой строке -- может цикл или функция?
task_2 = open("lesson_5_task_2.txt", "r", encoding="utf=8")

list_task_2 = list(task_2.readlines())
print(list_task_2)
print(f"Файл lesson_5_task_2.txt содержит", len(list_task_2), f"строк")

task_2.close()

task_2 = open("lesson_5_task_2.txt", "r", encoding="utf=8")
str_count = task_2.read()
print("В файле lesson_5_task_2.txt содержится ", len(str_count.split()), "слов")

task_2.close()



