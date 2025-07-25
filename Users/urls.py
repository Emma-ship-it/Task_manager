from django.urls import path
from django.contrib.auth.views import LoginView,LogoutView
from . import views
app_name = 'users'

urlpatterns =[
    path('signup/',views.signup,name ='signup'),
    path('login/',LoginView.as_view(template_name = 'Users/login.html'),name = 'login'),
    path('logout/',LogoutView.as_view(),name='logout')
]