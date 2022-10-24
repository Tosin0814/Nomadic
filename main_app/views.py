from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .forms import NewUserForm
from django.views.generic import ListView, DeleteView, DetailView, UpdateView, CreateView
from django.contrib import messages
from .models import User, Property, PropertyFeature, Photo, Availability, Like, Review


# Define the home view
# def index(request):
#   return render(request, 'property/index.html')

def choose_signup(request):
  return render(request, 'registration/choose_signup.html')


def signup(request):
  error_message = ''
  if request.method == 'POST':
    # Create a 'user' form object that includes the data from the browser
    form = NewUserForm(request.POST)
    if form.is_valid():
      # Add the user to the database
      user = form.save()
      # Login after signing up
      login(request, user)
      return redirect('profile_page', pk = user.id)
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = NewUserForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

  

class ProfilePage(DetailView):
  model = User
  template_name = 'user/profile.html'




# New code here
class ProfileView(DetailView):
  model = User
  template_name = 'user/profile.html'

class ProfileUpdate(UpdateView):
  model = User
  template_name = 'user/updateuser.html'
  fields = ['first_name', 'last_name', 'email']
  success_url = '/'

class ProfileDelete(DeleteView):
  model = User
  template_name = 'user/confirm_delete.html'
  success_url = '/'

class PropertyList(ListView):
  model = Property
  template_name = 'property/index.html'


def property_detail(request, property_id):
  property = Property.objects.get(id=property_id)
  # Add review form
  # Add property features not alredy on list
  return render(request, 'property/detail.html',{
    'property': property,
    # Pass review form
    # Pass property features
  })

class PropertyCreate(CreateView):
  model = Property
  fields = ['title', 'description', 'location', 'price']
  template_name = 'property/createproperty.html'
  def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class PropertyUpdate(UpdateView):
  model = Property
  fields = ['title', 'description', 'location', 'price']
  template_name = 'property/createproperty.html'

class PropertyDelete(DeleteView):
  model = Property
  template_name = 'property/confirm_delete.html'
  success_url = '/'