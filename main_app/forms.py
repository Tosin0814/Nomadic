from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.urls import reverse

from django.forms import ModelForm
from main_app.models import Availability



# Create your forms here.

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=50, required=True)
    last_name = forms.CharField(max_length=50, required=True)

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "password1", "password2")

# Add Availability

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