""" Routes for authentication app """
from django.urls import path

from . import views

app_name = 'authentication'
urlpatterns = [
    # login/
    path('login/',  views.login_view, name='login_view'),
    # register/
    path('register', views.register_view, name='register_view'),
    # try-login/
    path('try-login', views.try_login, name='login'),
    # try-register/
    path('try-register', views.try_register, name='register'),
    # logout/
    path('logout/', views.logout_view, name='logout'),
    # authenticated-view/
    path('authenticated-view/', views.authenticated_view, name='authenticated_view'),
    # authenticated-view-decorator/
    path('authenticated-view-decorator/', views.authenticated_view_with_decorator, name='authenticated_view_decorator')
]
