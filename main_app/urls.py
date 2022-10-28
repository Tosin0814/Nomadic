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
    path('profile/<int:pk>/', views.ProfileView.as_view(), name='profile_view'),
    path('profile/<int:pk>/update/', views.ProfileUpdate.as_view(), name='profile_update'),
    path('profile/<int:pk>/delete/', views.ProfileDelete.as_view(), name='profile_delete'),
    path('profile/<int:user_id>/add_profile_photo/', views.add_profile_photo, name='add_profile_photo'),
    path('property/<int:property_id>/', views.property_detail, name='property_detail'),
    path('property/create_property/', views.PropertyCreate.as_view(), name='create_property'),
    path('property/<int:pk>/update/', views.PropertyUpdate.as_view(), name='property_update'),
    path('property/<int:pk>/delete/', views.PropertyDelete.as_view(), name='property_delete'),
    
    path('property/<int:property_id>/associate_property_feature/<int:property_feature_id>/', views.associate_property_feature, name='associate_property_feature'),
    path('property/<int:property_id>/dissociate_property_feature/<int:property_feature_id>/', views.dissociate_property_feature, name='dissociate_property_feature'),
    path('property/<int:property_id>/add_photo/', views.add_photo, name='add_photo'),
    path('property/<int:property_id>/delete_photo/', views.delete_photo_page, name='delete_photo_page'),
    path('property/<int:property_id>/delete_photo/<int:photo_id>/', views.delete_photo, name='delete_photo'),

    # Add Availability
    path('property/<int:property_id>/add_availability/', views.add_availability, name="add_availability"),
    path('property/<int:property_id>/delete_availability/<int:availability_id>/', views.delete_availability, name='delete_availability'),
    path('property/<int:property_id>/<int:pk>/update/', views.AvailabiblityUpdate.as_view(), name="update_availability"),

    # Add Property Review
    path('property/<int:property_id>/review_property/', views.review_property, name='review_property'),

    # Host Profile
    path('property/<int:pk>/host_profile/', views.HostProfileView.as_view(), name='host_profile_view'),

    path('property/<int:property_id>/add_like', views.add_like,name="add_like"),
    path('property/<int:property_id>/add_unlike', views.add_unlike, name="add_unlike")
]
