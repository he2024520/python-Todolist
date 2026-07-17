# import json
#
# tasks = [
#     {
#         "name": "学习python",
#         "done": False
#
#     },
#     {"name": "打游戏", "done": False},
#     {"name": "休息", "done": False}
# ]
#
# with open("tasks.json", "w", encoding="utf-8") as file:
#     json.dump(tasks, file, ensure_ascii=False)
# import json
#
#
# def save_json(tasks):
#     with open("tasks.json", "w", encoding="utf-8") as file:
#         json.dump(tasks, file, ensure_ascii=False, indent=4)
#
#
# def load_taska():
#     try:
#         with open("tasks.json" ,"r", encoding="utf-8") as file:
#             content = json.load(file)
#             return content
#     except FileNotFoundError:
#        return []
# import json
# with open("lianxi.json", "w", encoding="utf-8") as f:
#     json.dump({"name": "he", "age": 12}, f, ensure_ascii = False)
#
# with open("lianxi.json", "r", encoding='utf-8') as g:
#     content = g.read()
#     content2 = json.loads(content)
#     print(content)
#     print(content2)

