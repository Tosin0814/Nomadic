from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

from django.views.generic import ListView, DeleteView, DetailView, UpdateView, CreateView

from .models import Profile, Property, PropertyFeature, Photo, Availability, Like, Review


# Define the home view
def index(request):
  return render(request, 'property/index.html')

def choose_signup(request):
  return render(request, 'registration/choose_signup.html')


def signup(request):
  error_message = ''
  if request.method == 'POST':
    # Create a 'user' form object that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # Add the user to the database
      user = form.save()
      # Login after signing up
      login(request, user)
      return redirect('create_profile', user_id = user.id)
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)



# def create_profile(request):
#   return render(request, 'profile/createprofile.html')

class CreateProfile(CreateView):
  model = Profile
  fields = ['first_name', 'last_name', 'email']
  