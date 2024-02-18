from django.urls import path
from .views import home, add_task, delete_task, edit_task

urlpatterns = [
    path('', home, name='home'),
    path('add-task/', add_task, name='add-task'),
    path('delete-task/<int:pk>/', delete_task, name='delete-task'),
    path('edit-task/<int:pk>/', edit_task, name='edit-task')
]
