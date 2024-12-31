import reflex as rx

class User(rx.Model, table=True):
    username: str
    email: str
    password: str

class Task(rx.Model,table=True):
    task_name:str
    task_description:str
    task_pay:float
    task_location:str
    task_time:str