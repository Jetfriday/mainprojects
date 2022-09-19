# ssh -L 19999:localhost:8401 apyatnitskiy@188.120.241.65
# vdv238hji
# jupyter notebook --port=8401
# http://localhost:19999/



# Создаём класс "Дело, которое сделано"
from distutils.command.sdist import sdist


class Todo:
    def __init__(Todo, task, planned_date, done_date):
        Todo.task = task
        Todo.planned_date = planned_date
        Todo.done_date = done_date
        
# Настраиваем текстовое сообщение о том, что задача записана.
#        print(f"Задача записана!")

# Настраиваем вывод инфо о задаче.
    def ShowExactTask(Todo):
        print(f"Задача {Todo.task} назначена на {Todo.planned_date}, исполнена {Todo.done_date}.")

# Считаем колличество записанных задач.
    def TotalNumberOfTasks(Todo):
        return 
        print(f"Задач в блокноте: .")

# Выводим список уникальных дел.
# 
    def UnicTasks(Todo):
        return 
        print(f"Список дел: .")        

# Считаем колличество повторов одного дела.
# Вводим таску, сраниваем её со следующей таской, если равны, то +1.
    def UnicTasksExecuteCount(Todo):
        return 
        print(f"Дела были выполнены, раз: .")

 # Считаем колличество дел сделанных по распианию.
 # Берём запланированную дату, вычетаем дату исполнения, если = 0, делаем +1.
    def OneDayTasksCount(Todo):
        return 
        print(f"One day gold signature task: .")       

Bread = Todo("Купить хлеб","2022-09-13","2022-09-14")
Work = Todo("Работа","2022-09-13","2022-09-14")
Travel = Todo("Путешествие","2022-09-13","2022-09-14")
Drink = Todo("Выпивка","2022-09-13","2022-09-14")
Sleep = Todo("Спать","2022-09-13","2022-09-14")
Ride = Todo("Катать","2022-09-13","2022-09-14")
Cinema = Todo("Кино","2022-09-13","2022-09-14")
Lunch = Todo("Поесть","2022-09-13","2022-09-14")

Todo.ShowExactTask(Lunch)

---------------------------

ToDo = ['Whiskey', 'Whiskey', 'buy_bread', 'Whiskey', 'Transfer', 'Transfer', 'Hard Work', 'Hard Work', 'Lanch', 'Sleep', 'Wakeup', 'SelfCare']
StartDate = ["2022-11-09", "2022-11-09", "2022-11-09", "2022-11-09", "2022-12-09", "2022-12-09", "2022-13-09", "2022-13-09", "2022-11-09", "2022-12-09", "2022-13-09", "2022-14-09"]
EndDate = ["2022-11-09", "2022-11-09", "2022-11-09", "2022-11-09", "2022-12-09", "2022-12-09", "2022-13-09", "2022-13-09", "2022-11-09", "2022-12-09", "2022-13-09", "2022-14-09"]

# Выводим общее кол-во дел.
print(len(ToDo)), "\n"

# Выводим перечисление дел.
# \n - оператор новой строки
print('\n'.join(map(str, ToDo))), "\n"

# Выводим дело 2 и 5.
print('Task 2: ' + ToDo[2])
print('Task 5: ' + ToDo[5]), "\n"

# Ищем совпадения с "buy bread".
def BuyBreadFinder(bb_cycle):
    for i in bb_cycle:
        if bb_cycle.count(i) == 'buy_bread':
            print(i)
            return True
    return False
    
if BuyBreadFinder(ToDo):
    print("No")
else:
    print("Yes"), "\n"
    
# Считаем длину строки дел.


Todo_List = ['Whiskey', 'Whiskey', 'buy_bread', 'Whiskey', 'Transfer', 'Transfer', 'Hard Work', 'Hard Work', 'Lanch', 'Sleep', 'Wakeup', 'SelfCare']
StartDate = ["2022-11-09", "2022-11-09", "2022-11-09", "2022-11-09", "2022-12-09", "2022-12-09", "2022-13-09", "2022-13-09", "2022-11-09", "2022-12-09", "2022-13-09", "2022-14-09"]
EndDate = ["2022-11-09", "2022-11-09", "2022-11-09", "2022-11-09", "2022-12-09", "2022-12-09", "2022-13-09", "2022-13-09", "2022-11-09", "2022-12-09", "2022-13-09", "2022-14-09"]

print('Exercise 1: print number of tasks.'), "\n"
print(len(Todo_List))

print('Task 2: ' + Todo_List[2])
print('Task 5: ' + Todo_List[5])