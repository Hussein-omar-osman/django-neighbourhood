from django.shortcuts import render

# Create your views here.

def home(request):

   return render(request, 'landing.html')
  
  
def loginPage(request):
   if request.method == 'POST':
     print(request.POST)
   return render(request, 'login.html')
  
def signupPage(request):
   if request.method == 'POST':
     print(request.POST)
   return render(request, 'signup.html')