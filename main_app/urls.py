from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/', views.choose_signup, name='choose_signup'),
    path('accounts/signup/', views.signup, name='signup'),
    path('profile/create/', views.create_profile, name='create_profile')
    # path('accounts/signup/', views.create_profile, name='create_profile'),
]
