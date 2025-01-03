import reflex as rx
from ..models import Task
from ..backend.backend import State
from ..components.navbar import navbar

def show_tasks(t: Task):
    """Show a customer in a table row."""

    return rx.table.row(
        rx.table.cell(t.task_name),
        rx.table.cell(t.task_description),
        rx.table.cell(t.task_pay),
        rx.table.cell(t.task_location),
        rx.table.cell(t.task_time),
    
        style={"_hover": {"bg": rx.color("gray", 3)}},
        align="center",
    )
def _header_cell(text: str, icon: str):
    return rx.table.column_header_cell(
        rx.hstack(
            rx.icon(icon, size=18),
            rx.text(text),
            align="center",
            spacing="2",
        ),
    )

def main_table():
    return rx.table.root(
            rx.table.header(
                rx.table.row(
                    _header_cell("Name", "list-todo"),
                    _header_cell("Descriptioon", "info"),
                    _header_cell("Payments", "dollar-sign"),
                    _header_cell("Address", "home"),
                    _header_cell("Time", "calendar"),
                ),
            ),
            rx.table.body(rx.foreach(State.tasks, show_tasks)),
            variant="surface",
            size="3",
            width="100%",
            on_mount=State.get_tasks,
            margin_top="5em",
        )


@rx.page(route="/tasks")
def tasks() -> rx.Component:
    return rx.flex(
        navbar(),
        main_table(),
        )