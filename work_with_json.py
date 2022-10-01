import json

data = {}
data['Todo_List'] = []
data['Todo_List'].append({
    'Task': 'Ride',
    'Planned_Date': '20-05-2022',
    'Done_Date': '2022-05-20'
})
data['Todo_List'].append({
    'Task': 'Drink',
    'Planned_Date': 'pythonist.ru',
    'Done_Date': 'Michigan'
})
data['Todo_List'].append({
    'Task': 'Smoke',
    'Planned_Date': 'pythonist.ru',
    'Done_Date': 'Alabama'
})
with open('data.json', 'w', encoding = 'utf-8') as outfile:
    json.dump(data, outfile, indent = 4)

# def write(data, filename):
#     data = json.dumps(data)
#     data = json.loads(str(data))
#     with open(filename, 'w', encoding = 'utf-8') as file:
#         json.dump(data, file, indent = 4)

# n_data = {
#     "users" : [1, 2, 3, 4]
# }

# write(n_data, 'data.json')