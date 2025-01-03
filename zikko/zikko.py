"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config
from .models import Task
from .components.navbar import navbar
from .pages.addtasks import addtasks
from .pages.home import home
from .pages.signup import signup
from .pages.tasks import tasks


app = rx.App()
# app.add_page(home)
# app.add_page(signup)
