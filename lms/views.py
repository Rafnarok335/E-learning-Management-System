from django.shortcuts import render
from django.shortcuts import redirect
from lms.models import LMS_User
def index(request):
    return render(request,'lms/index.html')
def dashboard(request):
    return render(request,'lms/dashboard.html')
def profile(request):
    return render(request,'lms/profile.html')
def login(request):
    user = request.POST['username']
    password = request.POST['password']
    lu = LMS_User.objects.all()
    if user in lu:
        u1 = LMS_User.objects.filter(User_Name=user)
        if u1.password == password:
            return redirect('dashboard') 
        else:
            return redirect('index')
    else:
        return redirect('index')
