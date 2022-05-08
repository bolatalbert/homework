rus_dict = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
with open("task_4_new.txt", "w", encoding="utf-8") as translated_file:
    with open("lesson_5_task_3.txt", encoding="utf-8") as old_file:
        translated_file.writelines([line.replace(line.split()[0], rus_dict.get(line.split()[0])) for line in old_file])
