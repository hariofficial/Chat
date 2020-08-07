from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name="login"),
    path('register.html', views.register, name="register"),
    path('home.html', views.homepage, name="homepage"),
    path('login.html',views.login,name='login'),
]
