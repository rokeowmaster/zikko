import reflex as rx
from ..models import Task
from ..components.navbar import navbar


class TaskState(rx.State):
    task_data:dict = {}

    @rx.event
    def task_submit(self, task_data:dict):
        self.task_data = task_data
        with rx.session() as session:

            session.add(
                Task(
                    **task_data
                )
            )
            session.commit()
            # if session.exec(
            #     select(Task).where(Task.id == self.current_user["email"])
            # ).first():
            #     return rx.window_alert("User with this email already exists")
            # self.task_data = Task(**task_data)
            # session.add(self.task_data)
            # session.commit()
            # session.refresh(self.task_data)


@rx.page(route="/addtasks")
def addtasks() -> rx.Component:
    return rx.vstack(
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

