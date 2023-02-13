from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.urls import reverse

from django.forms import ModelForm
from main_app.models import Availability, Review,Like


class NewUserForm(UserCreationForm):
    # email = forms.EmailField(required=True)
    # first_name = forms.CharField(max_length=50, required=True)
    # last_name = forms.CharField(max_length=50, required=True)
    
    def __init__(self, *args, **kwargs):
        super(NewUserForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "password1", "password2")
        widgets = {
            'username' : forms.TextInput(attrs={'class': 'form-control'}),
            'first_name' : forms.TextInput(attrs={'class': 'form-control'}),
            'last_name' : forms.TextInput(attrs={'class': 'form-control'}),
            'email' : forms.EmailInput(attrs={'class': 'form-control'}),
            'password1' : forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2' : forms.PasswordInput(attrs={'class': 'form-control'}),
        }


class DateInput(forms.DateInput):
    input_type = 'date'


class AvailabilityForm(ModelForm):
    class Meta:
        model = Availability
        fields = ["from_date","till_date"]
        widgets = {
            "from_date" : forms.DateInput(attrs = {'id' : 'id_from_date' , 'type' : 'date'}),
            "till_date" : forms.DateInput(attrs = {'id' : 'id_till_date' , 'type' : 'date'}), 
        }


class PropertyReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'review_text']
        widgets = {
            'rating': forms.Select(attrs={'class': 'form-control'}),
            'review_text' : forms.Textarea(attrs={'class': 'form-control'})
        }


class LikeForm(ModelForm):
    class Meta:
        model = Like
        fields = "__all__"

