from django.contrib import admin
from .models import Photo, Like, Review, PropertyFeature, Property, Availability, ProfilePicture

# Register your models here
admin.site.register(Photo)
admin.site.register(Property)
admin.site.register(ProfilePicture)
admin.site.register(Like)
admin.site.register(Review)
admin.site.register(PropertyFeature)
admin.site.register(Availability)