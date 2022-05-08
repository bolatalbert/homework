from random import randint

with open("lesson_5_task_5.txt", "w", encoding="utf-8") as task_5:
    new_list = [randint(1, 100) for _ in range(100)]
    task_5.write(" ".join(map(str, new_list)))

print(f"Сумма чисел - {sum(new_list)}")