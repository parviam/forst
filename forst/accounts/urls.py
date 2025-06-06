from django.urls import path
from . import views
urlpatterns = [
    path('signup', views.signup, name='accounts.signup'),
    path('login/', views.login, name='accounts.login'),
    path('logout/', views.logout, name='accounts.logout'),
    path('reset/', views.reset, name='accounts.reset'),
    path('verify/', views.verify_email, name='accounts.verify_email')
]