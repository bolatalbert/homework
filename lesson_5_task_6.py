new_dict = {}
with open("lesson_5_task_6.txt", "r", encoding="utf-8") as task_6:
    for line in task_6:
        name, stats = line.split(':')
        name_sum = sum(map(int, "".join([i for i in stats if i == ' ' or '9' >= i >= '0']).split()))
        new_dict[name] = name_sum
    print(f"{new_dict}")