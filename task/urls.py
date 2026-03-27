from django.urls import path
from .views import index, task_list, create_task, edit_task, delete_task

urlpatterns = [
    path('', index, name='index'),
    path('tasks/', task_list, name='tasks'),
    path('create_task/', create_task, name='create_task'),
    path('edit_task/', edit_task, name='edit_task'),
    path('delete_task/', delete_task, name='delete_task'),
]
