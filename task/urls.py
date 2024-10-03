from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home-view'),
    path('done/', views.task_done_view, name='task-done-view'),
    path('delete/', views.task_delete_view, name='task-delete-view'),
    path('done-delete/', views.done_delete_task_view, name='done-delete-task-view'),
    path('search/', views.search, name='search'),
    path('create-task/', views.create_task, name='create-task'),  # No id parameter here
    path('edit-task/', views.edit_task, name='edit-task'),
    path('done-task/', views.done_task, name='done-task'),
    path('delete-task/', views.delete_task, name='delete-task'),
]
