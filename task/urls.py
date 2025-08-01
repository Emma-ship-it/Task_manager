from django.urls import path
from . import views
app_name = 'task'
urlpatterns = [
    path('',views.home,name='home'),
    path('dashboard/',views.dashboard, name='dashboard'),
    path('task/<int:task_id>/',views.task_detail,name ='detail'),
    path('task/add_task/',views.add_task,name ="add"),
    path('edit/task/<int:id>/',views.edit_task,name='edit'),
    path('auth_delete/task/<int:id>/',views.confirm_delete,name ="confirm"),
    path('delete/task/<int:id>/',views.delete_task,name='delete')
]
