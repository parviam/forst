
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm, CustomErrorList
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.
@login_required
def logout(request):
    auth_logout(request)
    return redirect('home.index')

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, error_class=CustomErrorList)
        if form.is_valid():
            form.save()
            return redirect('accounts.login')
    else:
        form = CustomUserCreationForm(error_class=CustomErrorList)

    return render(request, 'accounts/signup.html', {'template_data': {'form': form}})

def login(request):
    template_data = {}
    template_data['title'] = 'Login'
    if request.method == 'GET':
        return render(request, 'accounts/login.html',
        {'template_data': template_data})
    elif request.method == 'POST':
        user = authenticate(
        request,
        username = request.POST['username'],
        password = request.POST['password']
        )
    if user is None:
        template_data['error'] = 'The username or password is incorrect.'
        return render(request, 'accounts/login.html',
        {'template_data': template_data})
    else:
        auth_login(request, user)
        return redirect('home.index')

def reset(request):
    template_data = {'title': 'Reset Password'}

    if request.method == 'GET':
        return render(request, 'accounts/reset.html', {'template_data': template_data})

    elif request.method == 'POST':
        username = request.session.get('reset_username')
        if not username:
            template_data['error'] = 'Session expired. Please verify your email again.'
            return redirect('accounts.verify_email')

        try:
            user = User.objects.get(username=username)
            new_password = request.POST.get('password')
            user.set_password(new_password)
            user.save()
            del request.session['reset_username']
            return redirect('accounts.login')
        except User.DoesNotExist:
            template_data['error'] = 'Unexpected error. Please try again.'
            return render(request, 'accounts/reset.html', {'template_data': template_data})
    
def verify_email(request):
    template_data = {'title': 'Verify Email'}
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            user = User.objects.get(email=email)
            request.session['reset_username'] = user.username  # store securely in session
            return redirect('accounts.reset')
        except User.DoesNotExist:
            template_data['error'] = 'No user found with that email address.'
    return render(request, 'accounts/verify.html', {'template_data': template_data})

