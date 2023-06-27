from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import ImageForm
from .models import ImageModel
from django.contrib.auth.models import User

def dashboard_login(request):
    if request.method == 'POST':
        print(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None :
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password', extra_tags='login-error')  # Send an alert message
    return render(request, 'login.html')

def dashboard_register(request):
    return render(request, 'register.html')

def dashboard_logout(request):
    logout(request)
    return redirect('home')


@login_required
def dashboard(request):
    count = ImageModel.objects.all().count()
    users = User.objects.all().count()
    return render(request, 'dashboard.html',context={"imagecount":count,"users":users})

@login_required
def image_upload(request):
    print('Uploading',request.method)
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        print(form.is_valid())
        if form.is_valid():
            for image in request.FILES.getlist('image'):
                img = ImageModel.objects.create(image=image)
                messages.success(request, 'Images uploaded successfully!')
    return render(request, 'imageupload.html')


@login_required
def list_images(request):
    data = ImageModel.objects.all()
    return render(request, 'listimages.html',context={'images':data})