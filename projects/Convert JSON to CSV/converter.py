import json
import csv


with open('/Users/amadoudiallo/Workspace/python-mini-projects/projects/Convert JSON to CSV/input.json', 'r') as f:
    data = json.load(f)
    fin = f'{", ".join(list(data[0].keys()))}'

    for i in data:
        fin += f'\n{i["Name"]}, {i["age"]}, {i["birthyear"]}'
print(fin)

with open('out.csv', 'w') as o:
    o.write(fin)
