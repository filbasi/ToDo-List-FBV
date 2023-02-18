from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.main_view, name='task_list'),
    path('create/', views.task_create, name='create_task'),
    path('detail/<int:pk>', views.task_detail, name='detail_task'),
    path('delete/<int:pk>', views.task_delete, name='delete_task'),
    path('update/<int:pk>', views.task_update, name='update_task'),
]