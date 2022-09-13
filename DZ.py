# Создаём класс "Дело, которое сделано"
class Todo:
    def __init__(Todo, what_to_do, planned_date, done_date):
        Todo.what_to_do = what_to_do
        Todo.planned_date = planned_date
        Todo.done_date = done_date
        
# Настраиваем текстовое сообщение о том, что задача записана.
        print(f"Задача записана!")

# Настраиваем вывод инфо о задаче.
    def show(Todo):
        print(f"Задача {Todo.what_to_do} назначена на {Todo.planned_date}, исполнена {Todo.done_date}.")

Bread = Todo("Купить хлеб","2022-09-13","2022-09-14")

Todo.show(Bread)
