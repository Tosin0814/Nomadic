from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/', views.choose_signup, name='choose_signup'),
    path('accounts/signup/', views.signup, name='signup'),
    path('profile/<int:pk>/', views.ProfilePage.as_view(), name='profile_page'),
]
