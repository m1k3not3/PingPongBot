import json

with open('banned.json', 'r') as f:
    data = json.load(f)
    data.append("izi")

with open('banned.json', 'w') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

with open('banned.json', 'w') as f:
    json.remove

print(data)