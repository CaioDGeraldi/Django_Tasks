from django.urls import path
from .views import index, task_list, create_task, edit_task, delete_task

urlpatterns = [
    path('', index, name='index'),
    path('tasks/', task_list, name='tasks'),
    path('create/', create_task, name='create'),
    path('edit/<int:id>', edit_task, name='edit'),
    path('delete/<int:id>', delete_task, name='delete'),
]
