from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

TYPE = (
    ('H', 'Host'),
    ('R', 'Renter')
)

class SignUpForm(UserCreationForm):
    type = forms.CharField(
        max_length=10,
        choices = TYPE,
        )

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', )

    def __str__(self):
        # Nice method for obtaining the friendly value of a Field.choice
        return f"{self.get_type_display()}"