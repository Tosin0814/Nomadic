from django.urls import path
from . import views

urlpatterns = [
    ## View Function removed
    # path('', views.index, name='index'),
    path('accounts/', views.choose_signup, name='choose_signup'),
    path('accounts/signup/', views.signup, name='signup'),
    path('profile/<int:pk>/', views.ProfilePage.as_view(), name='profile_page'),

    # Added paths
    path('', views.PropertyList.as_view(), name='home'),
    path('<int:property_id>/', views.property_detail, name='property_detail'),
    path('create_property/', views.PropertyCreate.as_view(), name='create_property'),
    path('<int:pk>/update/', views.PropertyUpdate.as_view(), name='property_update'),
    path('<int:pk>/delete/', views.PropertyDelete.as_view(), name='property_delete'),
    path('profile/<int:pk>/', views.ProfileView.as_view(), name='profile_view'),
    path('profile/<int:pk>/update/', views.ProfileUpdate.as_view(), name='profile_update'),
    path('profile/<int:pk>/delete/', views.ProfileDelete.as_view(), name='profile_delete'),
    path('<int:property_id>/associate_property_feature/<int:property_feature_id>/', views.associate_property_feature, name='associate_property_feature'),
    path('<int:property_id>/dissociate_property_feature/<int:property_feature_id>/', views.dissociate_property_feature, name='dissociate_property_feature'),
    path('<int:property_id>/add_photo/', views.add_photo, name='add_photo'),
    path('profile/<int:user_id>/add_profile_photo/', views.add_profile_photo, name='add_profile_photo'),
]
