from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import ProfilePictureForm, UserLoginForm
from .models import StudentProfile
from . forms import ContactForm
from .models import Course

@login_required
def settings(request):
    user = request.user
    try:
        student_profile = user.studentprofile
    except StudentProfile.DoesNotExist:
        student_profile = StudentProfile.objects.create(user=user)

    if request.method == 'POST':
        form = ProfilePictureForm(request.POST, request.FILES, instance=student_profile)
        if form.is_valid():
            form.save()
            # Update username if it's changed
            new_username = request.POST.get('username')
            if new_username and new_username != user.username:
                user.username = new_username
                user.save()
            return redirect('index')
    else:
        form = ProfilePictureForm(instance=student_profile, initial={'username': user.username})
    return render(request, 'settings.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            auth_login(request, user)
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def home(request):
    return render(request, 'home.html')

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('index')
    else:
        form = UserLoginForm()
    return render(request, 'registration/login.html', {'form': form})

@login_required
def index(request):
    try:
        student_profile = request.user.studentprofile
    except StudentProfile.DoesNotExist:
        student_profile = None

    context = {
        'user': request.user,
        'student_profile': student_profile,
    }
    return render(request, 'index.html', context)

def profile_view(request):
    user = request.user
    try:
        student_profile = user.studentprofile
    except StudentProfile.DoesNotExist:
        student_profile = None
    return render(request, 'profile.html', {'student_profile': student_profile})


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # Save form data to the database
            return redirect('success')  # Redirect to success page
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})
def success(request):
    return render(request, 'success.html')

def search_list(request):
    query = request.GET.get('q')
    if query:
        courses = Course.objects.filter(name__icontains=query)
    else:
        courses = Course.objects.all()
    return render(request, 'courses/course_list.html', {'courses': courses})