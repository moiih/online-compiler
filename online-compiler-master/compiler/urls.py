from django.urls import path
from . import views


urlpatterns = [
    path('', views.compile, name='home'),
    # path('login/', views.login, name='login'),
    # path('register/', views.register, name='register'),
    # path('get_code/<int:id>/', views.get_code, name='get_code'),
    path('logout/', views.logout, name='logout'),    
]
