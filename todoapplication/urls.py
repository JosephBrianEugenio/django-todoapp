from django.contrib import admin
from django.urls import path,re_path
from mytodoapp.api.version.v1.task.task_list.views.task_list_views import ListTaskAPI
from mytodoapp.api.version.v1.board.board_list.views.board_list_views import ListBoardAPI
from mytodoapp.api.version.v1.board.create_board.views.create_board_views import CreateBoardAPI
from mytodoapp.api.version.v1.board.edit_board.views.edit_board_views import EditBoardAPI
from mytodoapp.api.version.v1.board.delete_board.views.delete_board_views import DeleteBoardAPI

# task
from mytodoapp.api.version.v1.task.create_task.views.create_task_views import CreateTaskAPI
from mytodoapp.api.version.v1.task.edit_task.views.edit_task_views import EditTaskAPI
from mytodoapp.api.version.v1.task.delete_task.views.delete_task_views import DeleteTaskAPI




urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('api/edit_board/', EditBoardAPI.as_view(), name='user_edit_board'),
    path('api/boards/list/', ListBoardAPI.as_view(), name='user_list_board'),
    path('api/create_board/', CreateBoardAPI.as_view(), name='user_create_board'),
    re_path('api/delete_board/', DeleteBoardAPI.as_view(), name='user_delete_board'),
# task
    path('api/tasks/list/', ListTaskAPI.as_view(), name='user_list_task'),
    re_path('api/create_task/', CreateTaskAPI.as_view(), name='user_create_task'),
    re_path('api/edit_task/', EditTaskAPI.as_view(), name='user_edit_task'),
    re_path('api/delete_task/', DeleteTaskAPI.as_view(), name='user_delete_task')
]
