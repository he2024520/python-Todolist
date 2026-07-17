import json


def save_tasks(tasks):
    with open("tasks3.json", "w", encoding="utf-8") as file:
        json.dump(tasks, file, ensure_ascii=False, indent=4)

def load_tasks():
    try:
        with open("tasks3.json" ,"r", encoding="utf-8") as file:
            content = json.load(file)
            return content
    except FileNotFoundError:
        return []

tasks = load_tasks()

def add_task(tasks):
    name = input("请输入需要添加的任务\n")

    task = {"name": name, "done": False}
    tasks.append(task)
    save_tasks(tasks)

def show_tasks(tasks):
    if len(tasks) == 0:
        print("当前暂时没有任务")
        return
    for index, task in enumerate(tasks):
        if task["done"] == False:
            print(index, task["name"], "❌️")
        else:
            print(index, task["name"], "✅️")

def complete_tasks(tasks):
    if len(tasks) == 0:
        return

    try:
        index = int(input("输入你需要修改的任务状态的编号\n"))
        if 0 <= index < len(tasks):
            tasks[index]["done"] = not tasks[index]["done"]
            print("修改成功！")
            save_tasks(tasks)
        else:
            print("超出正常数字范围")
    except ValueError:
        print("请输入正确有效的数字")


def del_task(tasks):
    if len(tasks) == 0:
        return

    try:
        index = int(input("请输入你需要删除的编号\n"))
        if 0 <= index < len(tasks):
            deleted = tasks.pop(index)
            print(f"已删除任务{deleted}")
            show_tasks(tasks)
    except ValueError:
        print("请输入正确有效的数字")
    save_tasks(tasks)

def ChangeName_task(tasks):
    if len(tasks) == 0:
        return

    index = int(input("输入需要修改的任务编号\n"))
    if 0 <= index < len(tasks):
        new_name = str(input("输入修改后任务名称"))
        tasks[index]["name"] = new_name
        print("修改成功！")
        save_tasks(tasks)

def search_task(tasks):
    if len(tasks) == 0:
        return
    found = False
    key_word = str(input("输入你想要查找的任务关键词\n"))

    if not found:
        for index, task in enumerate(tasks):
            if key_word in task["name"]:
                found = True
                if task["done"] == False:
                    print(index, task["name"], "❌️")
                else:
                    print(index, task["name"], "✅️")


    if found == False:
            print("没有找到")


while True:
    print("======Todolist=======")
    print("1.增加任务")
    print("2.改变任务状态")
    print("3.删除任务")
    print("4.展示任务")
    print("5.改变任务名称")
    print("6.查找任务")
    print("7.退出")


    choise = input("接下来你将选择什么功能\n")
    if choise == "1":
        add_task(tasks)
    elif choise == "2":
        complete_tasks(tasks)
    elif choise == "3":
        del_task(tasks)
    elif choise == "4":
        show_tasks(tasks)
    elif choise == "5":
        ChangeName_task(tasks)
    elif choise == "6":
        search_task(tasks)
    elif choise == "7":
        break

    else:
        print("无效输入")