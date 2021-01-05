from django.urls import path
from . import views

urlpatterns = [
    # path('', views.hello_world, name='hello_world'),
    path('task_list/', views.TaskList, name='Tasks_List'),
    path('create_task/', views.CreateTask, name='Create_Task'),
    path('update_task/<str:pk>/', views.UpdateTask, name='Update_Task'),
    path('task_detail/<str:pk>/', views.TaskDetail, name='Create_Task'),
    path('delete_task/<str:pk>/', views.DeleteTask, name='Create_Task'),

]
