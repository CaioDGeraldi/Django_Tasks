from django.urls import path, include
from .views import task_list, create_task, edit_task, delete_task

urlpatterns = [
    path('', task_list, name='index'),
    path('create/', create_task, name='create'),
    path('edit/<int:id>', edit_task, name='edit'),
    path('delete/<int:id>', delete_task, name='delete'),
    path('accounts/', include('django.contrib.auth.urls')),
]
