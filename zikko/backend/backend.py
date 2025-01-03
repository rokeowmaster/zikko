import reflex as rx
from ..models import Task
from ..models import User

class State(rx.State):
    tasks: list[Task]=[]

    def get_tasks(self):
        with rx.session() as session:
            self.tasks = session.exec(
                Task.select()
            ).all()

    # def create_users(self, user_data):
    #     with rx.session() as session:
    #         session.add(
    #             User(
    #                 **user_data
    #             )
    #         )
    #         session.commit()