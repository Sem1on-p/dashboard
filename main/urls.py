from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
	path('', views.void, name='void'),
	path('dashboard', views.dashboard, name='dashboard'),
	path('dashboard/potential', views.potential, name='potential'),
	path('dashboard/job', views.job, name='job'),
	path('dashboard/end_event', views.end_event, name='end_event'),
	path('dashboard/event/id<int:event_id>', views.view_event, name='view_event'),
	path('tasks', views.tasks, name='tasks'),
	path('tasks/archive', views.tasks_archive, name='tasks_archive'),
	path('tasks/delete/<int:task_id>', views.delete_task, name='delete_task')
]