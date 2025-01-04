from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('task_detail/<int:id>/', views.task_detail, name='task_detail'),
    path('task_delete/<int:id>/', views.task_delete, name='task_delete'),
    path('task_update/<int:id>/', views.task_update, name='task_update'),
    path('create_task/', views.create_task, name='create_task')
]
