"""task_manager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from boards import views as api_views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', TokenObtainPairView.as_view(), name='api-login'),
    path('rigester/', api_views.Rigester.as_view(), name='api-register'),
    path('boards/create/', api_views.BoardCreate.as_view(), name='board-create'),
    path('boards/', api_views.BoardList.as_view(), name='board-list'),
    path('TaskList/', api_views.TaskList.as_view(), name='task-list'),
    path('TaskListOtherUser/', api_views.TaskListOtherUser.as_view(), name='Task-list2'),
    path('TaskList/?ordering=creation_date', api_views.TaskList.as_view(), name='task-list'),
    path('boards/<int:board_id>/delete/', api_views.DeleteBoard.as_view(), name="delete-board"),
    path('task/<int:task_id>/delete/', api_views.DeleteTask.as_view(), name="delete-task"),
    path('add/task/<int:board_id>/',api_views.AddTask.as_view(), name='add-task')
]
