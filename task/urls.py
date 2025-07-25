from django.urls import path
from . import views
app_name = 'task'
urlpatterns = [
    path('home',views.home,name='home'),
    path('dashboard',views.dashboard, name='dashboard')
]
