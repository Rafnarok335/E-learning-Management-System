from django.shortcuts import render
def index(request):
    return render(request,'lms/index.html')
def dashboard(request):
    return render(request,'lms/dashboard.html')
def profile(request):
    return render(request,'lms/profile.html')