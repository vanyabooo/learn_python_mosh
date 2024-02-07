"""
def - функция
return - заключает функцию и назад что-то выдает
print(type()) - полезная функция для дебагинга, показывает тип переменной
"""


import time
name = "doki"
current_time = time.time()
student = "vanya"
def repetitive_task_1():
    print(name)
    print(current_time)
    print(student)

repetitive_task_1()

def square_my_num(x):
    print(x * x)
    return x

square_my_num(10)