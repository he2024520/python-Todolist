import json
with open("tasks.json", "r", encoding="utf-8") as file:
    content = json.load(file)
print(content)