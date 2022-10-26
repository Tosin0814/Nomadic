from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .forms import NewUserForm, AvailabilityForm, PropertyReviewForm
from django.views.generic import ListView, DeleteView, DetailView, UpdateView, CreateView
from django.contrib import messages
from .models import ProfilePicture, User, Property, PropertyFeature, Photo, Availability, Like, Review


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
import uuid
import boto3

S3_BASE_URL = 'https://s3-ca-central-1.amazonaws.com/'
BUCKET = 'nomadic-project'

class ProfileView(DetailView):
  model = User
  template_name = 'user/profile.html'

class ProfileUpdate(UpdateView):
  model = User
  template_name = 'user/updateuser.html'
  fields = ['email']
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
  property_review_form = PropertyReviewForm
  features_property_doesnt_have = PropertyFeature.objects.exclude(id__in = property.property_features.all().values_list('id'))
  availability_form = AvailabilityForm()
  return render(request, 'property/detail.html',{
    'property': property,
    'features_property_doesnt_have': features_property_doesnt_have,
    'availability_form' : availability_form,
    'property_review_form' : property_review_form
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

def associate_property_feature(request, property_id, property_feature_id):
  Property.objects.get(id=property_id).property_features.add(property_feature_id)
  return redirect('property_detail', property_id=property_id)

def dissociate_property_feature(request, property_id, property_feature_id):
  Property.objects.get(id=property_id).property_features.remove(property_feature_id)
  return redirect('property_detail', property_id=property_id)

def add_photo(request, property_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        # need a unique "key" for S3 / needs image file extension too
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            # build the full url string
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            # we can assign to property_id or property (if you have a property object)
            photo = Photo(photo_url=url, property_id=property_id)
            photo.save()
        except:
            print('An error occurred uploading file to S3')
    return redirect('property_detail', property_id=property_id)


def add_profile_photo(request, user_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        # First delete previous photo (Only one photo is allowed)
        existing_photos = ProfilePicture.objects.filter(user_id=user_id)
        if existing_photos:
            existing_photos.delete()
        s3 = boto3.client('s3')
        # need a unique "key" for S3 / needs image file extension too
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            # build the full url string
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            # we can assign to user_id or user (if you have a user object)
            profile_picture = ProfilePicture(url=url, user_id=user_id)
            profile_picture.save()
        except:
            print('An error occurred uploading file to S3')
    return redirect('profile_view', pk=user_id)

# Add Availability

def add_availability(request, property_id):
  form = AvailabilityForm(request.POST)
  if form.is_valid():
    new_availbility = form.save(commit=False)
    new_availbility.property_id = property_id
    new_availbility.save()
  return redirect('property_detail', property_id = property_id)

def delete_availability(request, property_id, availability_id):
  Property.objects.get(id = property_id).availability_set.filter(id = availability_id).delete()
  return redirect('property_detail', property_id = property_id)

class AvailabiblityUpdate(UpdateView):
  model = Availability
  form_class = AvailabilityForm
  template_name = 'property/availability_form.html'


# Add Property Review

def review_property(request, property_id):
    form = PropertyReviewForm(request.POST)
    if form.is_valid():
        new_review = form.save(commit=False)
        new_review.user_name = request.user.username
        new_review.property_id = property_id
        new_review.save()
    return redirect('property_detail', property_id = property_id)