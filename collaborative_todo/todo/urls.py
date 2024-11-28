from django.urls import path
from .views import TaskList, task_list, add_task, toggle_task, delete_task

urlpatterns = [
    # API routes for the extension or external apps
    path('api/tasks/', TaskList.as_view(), name='task_list_api'),
    path('api/tasks/<int:task_id>/', delete_task, name='delete_task'),  # Ensure this is the correct path
    path('', task_list, name='task_list'),
    path('add-task/', add_task, name='add_task'),
    path('toggle-task/<int:task_id>/', toggle_task, name='toggle_task'),
    path('delete-task/<int:task_id>/', delete_task, name='delete_task'),
]
