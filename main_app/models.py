from enum import auto
from django.db import models
from django.forms import DateField
from django.urls import reverse
from datetime import datetime, date  
from django.contrib.auth.models import User


FEATURES = (
    ('W', 'WIFI'),
    ('TV', 'HDTV'),
    ('WF', 'Waterfront'),
    ('CAC', 'Central Air Conditioning'),
    ('BS', 'Bluetooth Sound System'),
    ('BG', 'Board Games'),
    ('CH', 'Central heating'),
    ('P', 'Pool'),
)

RATINGS = (
    ('E', 'Excellent'),
    ('VG', 'Very Good'),
    ('G', 'Good'),
    ('A', 'Average'),
    ('B', 'Bad'),
    ('VB', 'Very Bad'),
    ('S', 'Stay Away')
)

class ProfilePicture(models.Model):
    url = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        # For obtaining the friendly value of a Field.choice
        return f"Photo created on {self.date_created}"


class PropertyFeature(models.Model):
    feature = models.CharField(
        max_length=3,
        choices = FEATURES,
    )
    
    def __str__(self):
        return f"{self.get_feature_display()}"
    
    class Meta:
        ordering = ['feature']


class Property(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=800)
    location = models.CharField(max_length=100)
    property_features = models.ManyToManyField(PropertyFeature)
    date_listed = models.DateField(auto_now_add=True)

    def __str__(self):
        # Nice method for obtaining the friendly value of a Field.choice
        return f"{self.title} on {self.date_listed}"

    class Meta:
        ordering = ['-date_listed']


class Photo(models.Model):
    photo_url = models.CharField(max_length=200)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        # For obtaining the friendly value of a Field.choice
        return f"Photo created on {self.date_created}"

    class Meta:
        ordering = ['date_created']


class Availability(models.Model):
    from_date = models.DateField('Available from')
    till_date = models.DateField('Available till')
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    
    def __str__(self):
        # Nice method for obtaining the friendly value of a Field.choice
        return f"{self.from_date} to {self.till_date}"

    class Meta:
        ordering = ['from_date']


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)


class Review(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    rating = models.CharField(
        max_length=2,
        choices = RATINGS,
    )
    review_text = models.TextField(max_length=800)
    date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        # Nice method for obtaining the friendly value of a Field.choice
        return f"{self.get_rating_display()} on {self.date}"