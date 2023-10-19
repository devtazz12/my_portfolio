from django.shortcuts import render, redirect
from .models import *

# Create your views here.

def index(request):
    return render(request, 'index.html')

def contact(request):
    if request.method == "POST":
        fname=request.POST['fname']
        email=request.POST['email']
        subject=request.POST['subject']
        message=request.POST['message']

        user_message= ContactMe.objects.create(
            fname=fname,
            email=email,
            subject=subject,
            message=message,
        )
        user_message.save()
    return redirect('home')

def error_404(request, exception):
    return redirect('home')
