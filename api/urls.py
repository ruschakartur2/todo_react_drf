from django.urls import path
from . import views
from .views import TaskViewSet

taskList = TaskViewSet.as_view({'get': 'list'})
taskDetail = TaskViewSet.as_view({'get': 'retrieve'})
taskUpdate = TaskViewSet.as_view({'post': 'update'})

taskDelete = TaskViewSet.as_view({'delete': 'destroy'})

urlpatterns = [
    path('', views.apiOverview, name="api-overview"),
    path('task-list/', taskList, name="task-list"),
    path('task-detail/<int:pk>/', taskDetail, name="task-detail"),
    path('task-update/<int:pk>/', taskUpdate, name='task-update'),
    path('task-delete/<int:pk>/', taskDelete, name="task-delete"),
]
