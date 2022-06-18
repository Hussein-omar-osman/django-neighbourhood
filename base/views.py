from django.shortcuts import render, redirect
from django.contrib import messages
from base.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout


# Create your views here.

def home(request):

   return render(request, 'landing.html')
  
def loginPage(request):
   if request.user.is_authenticated:
     return redirect('home')
   if request.method == 'POST':
     email = request.POST['email'].lower()
     password = request.POST['password']
     print(email)
     print(password)
     try:
         user = User.objects.get(email=email)
     except:
         messages.error(request, 'User not exist.')
         
     user = authenticate(request, email=email, password=password)
     if user:
         login(request, user)
         
         return redirect('home')
     else:
         messages.error(request, 'Email or password incorrect.')
   return render(request, 'login.html')
  

def registerPage(request):
   if request.user.is_authenticated:
       return redirect('home')
   
   context = {'form':'form'}
   if request.method == 'POST':
        if User.objects.filter(username=request.POST['username']).exists():
          messages.info(request, 'Username is taken')
          return render(request, 'register.html')
        elif User.objects.filter(email=request.POST['email']).exists():
          messages.info(request, 'Email is taken')
          return render(request, 'register.html')
        elif request.POST['password1'] != request.POST['password2']:
          messages.info(request, 'Password and Confirm Password do not match')
          return render(request, 'register.html')
        elif request.POST['neighboor'] == 'no' :
          messages.info(request, 'Select a neighboorhood')
          return render(request, 'register.html')
        elif len(request.POST['password1']) < 8 or request.POST['password1'] == request.POST['username']:
          messages.info(request, 'Password length must be > 9 & not the same as username')
          return render(request, 'register.html')
        else:
           print('you have reached user creating')
           print(request.POST)
           user = User.objects.create_user(username=request.POST['username'], email=request.POST['email'], password=request.POST['password1'], neighboorhood=request.POST['neighboor'])
           user.save()
           login(request, user)
           return redirect('home')
         #   form = MyCreateUserForm(request.POST)
         #   if form.is_valid():
         #       user = form.save(commit=False)
         #       user.username = user.username.lower()
         #       user.email = user.email.lower()
         #       user.save()
         #       login(request, user)
         #       return redirect('home')       
         #   else:
         #     messages.error(request, 'An error ocurred during registration.')
          
   return render(request, 'register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home')