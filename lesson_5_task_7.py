import json

with open("lesson_5_task_7.json", "w", encoding="utf-8") as write_task_7, open("lesson_5_task_7.txt", encoding="utf-8") as read_task_7:
    profit = {line.split()[0]: int(line.split()[2] - int(line.split()[3]) for line in read_task_7)}
    f_up = [int(i) for i in profit.values() if int(i) > 0]
    result = [profit, {"average_profit": round(sum(f_up) / len(f_up))}]

    json.dump(result, write_task_7, ensure_ascii=False, indent=4)
