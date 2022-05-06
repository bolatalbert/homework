# ---- Задание 3 ----

little_salary = open("lesson_5_task_3.txt", "r", encoding="utf-8")
sal_dict = {line.split()[0]: float(line.split()[1]) for line in little_salary}
print(f"Average salary = {round(sum(sal_dict.values()) / len(sal_dict), 3)}\n"
      f'Salary less than 20k {[e[0] for e in sal_dict.items() if e[1] < 20000]}')


little_salary.close()
