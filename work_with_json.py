import json
from pprint import pprint
from random import randint as rd, choice as ch


def write(data, json_file):
    data = json.dumps(data)
    data = json.loads(str(data))
    with open(json_file, 'w', encoding = 'utf-8') as file:
        json.dump(data, file, indent = 4)

def read(json_file):
    with open(json_file, 'r', encoding = 'utf-8') as file:
        return json.load(file)

class Task:
    def __init__(self):
        self.task = ch(['First', 'Second', 'Third'])
        self.planned_date = rd(0, 70)
        self.done_date = rd(0, 1000)

        print(f"Дело записано в лист: {self}")

#Ride = Task('Ride','Today', 'Taday2')

data = {
    'tasks' : []
}

for i in range(100):
    data['tasks'].append(Task().__dict__)

write(data, 'data.json')

# n_data = read('data.json')
# print(n_data['tasks'][0][1])
# input()
