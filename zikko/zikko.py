"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config
from .models import Task
from .components.navbar import navbar

class State(rx.State):
    """The app state."""

    ...

class FormState(rx.State):
    form_data:dict = {}

    @rx.event
    def submit(self, form_data:dict):
        self.form_data = form_data

class TaskState(rx.State):
    task_data:Task | None = None

    @rx.event
    def task_submit(self, task_data:dict):
        with rx.session() as session:
            # if session.exec(
            #     select(Task).where(Task.id == self.current_user["email"])
            # ).first():
            #     return rx.window_alert("User with this email already exists")
            self.task_data = Task(**task_data)
            session.add(self.task_data)
            session.commit()
            session.refresh(self.task_data)

@rx.page(route="/")
def home() -> rx.Component:
    # Welcome Page (Index)
    return rx.box(
        navbar(),
        rx.text("Main content")
        )
    

@rx.page(route="/tasks")
def tasks() -> rx.Component:
    return rx.text("Task page")

@rx.page(route="/addtasks")
def addtasks() -> rx.Component:
    return rx.box(
            navbar(),
            rx.center(
            rx.card(
            rx.vstack(
                rx.heading("Add New Task"),
                rx.form(
                rx.hstack(
                    rx.text("Task"),
                    rx.input(
                            name="task_name",
                            required=True,
                        ),
                    rx.text("Description"),
                    rx.input(
                            name="task_description",
                            required=True,
                        ),
                    rx.text("Pay"),
                    rx.input(
                            name="task_pay",
                            required=True,
                        ),
                    rx.text("Location"),
                    rx.input(
                            name="task_location",
                            required=True,
                        ),
                    rx.text("Time"),
                    rx.input(
                            name="task_time",
                            required=True,
                        ),
                    rx.button("Post Task")
                    ),
                    on_submit=TaskState.task_submit
                )
            ),
            rx.text(TaskState.task_data.to_string()),
            margin_top="5em"
        )
    )
        )



def signup():
    return rx.card(
        rx.vstack(
            rx.center(
                rx.form(
                    
                    rx.heading("Join"),                        
                
                    rx.vstack(
                        rx.text(
                            "Name ",
                            rx.text.span("*", color="red"),
                        ),
                        rx.input(
                            name="name",
                            required=True,
                        ),
                    ),
                    rx.vstack(
                        rx.text(
                            "Email ",
                            rx.text.span("*", color="red"),
                        ),
                        rx.input(
                            name="email",
                            type="email",
                            required=True,
                        ),
                    ),
                    rx.vstack(
                        rx.text(
                            "Password",
                            rx.text.span("*", color="red"),
                        ),
                        rx.input(
                            name="password",
                            type="password",
                            required=True,
                        ),
                    ),
                   
                    rx.button("Send", type="submit"),
                    on_submit=FormState.submit
                    )
                )
            ),
            rx.text(FormState.form_data.to_string())
        )


    


app = rx.App()
app.add_page(home)
app.add_page(signup)
