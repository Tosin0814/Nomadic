from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/', views.choose_signup, name='choose_signup'),
    path('accounts/signup_host/', views.signup_host, name='signup_host'),
    path('accounts/signup_renter/', views.signup_renter, name='signup_renter'),
    path('profile/create/', views.create_profile, name='create_profile')
    # path('accounts/signup/', views.create_profile, name='create_profile'),
]
