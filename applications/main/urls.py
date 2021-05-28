from django.urls import path

#local
from . import views

app_name = 'main_app'

urlpatterns = [
    path('create-user/', views.CreateUser.as_view(), name = 'create_user'),
    path('login-user/', views.LoginUser.as_view(), name = 'login_user'),
    path('favorite-candidate/<pk>/', views.UpdateVote.as_view(), name = 'favorite_candidate'),
]