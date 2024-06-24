from django.contrib import admin
from mytodoapp.models.board_model import Board
from mytodoapp.models.task_model import Task



admin.site.register(Board)
admin.site.register(Task)