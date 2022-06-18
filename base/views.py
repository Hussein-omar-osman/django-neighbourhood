from django.shortcuts import render, redirect
from django.contrib import messages
from base.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout


# Create your views here.

def home(request):

   return render(request, 'landing.html')
  
  
def loginPage(request):
   if request.method == 'POST':
     print(request.POST)
   return render(request, 'login.html')
  
# def registerPage(request):
#    if request.method == 'POST':
#       username = request.POST.get('username').lower()
#       email = request.POST.get('email').lower()
#       neighboor = request.POST.get('neighboor')
#       password = request.POST.get('password1')
#       password2 = request.POST.get('password2')
#       print(username, email, neighboor, password, password2)
#       if User.objects.filter(username=username).exists():
#          messages.info(request, 'Username is taken')
#          return redirect('registerPage')
#       elif User.objects.filter(email=request.POST['email']).exists():
#          messages.info(request, 'Email is taken')
#          return redirect('registerPage')
#       elif request.POST['password1'] != request.POST['password2']:
#          messages.info(request, 'Password and Confirm Paswword dont match')
#          return redirect('registerPage')
#       else:
#          print('creating user')
#             # user = User.objects.create_user
#             # user.username = user.username.lower()
#             # user.email = user.email.lower()
#             # user.save()
#             # return redirect('home')       
#          # else:
#          #    messages.error(request, 'An error ocurred during registration.')
#    return render(request, 'signup.html')

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