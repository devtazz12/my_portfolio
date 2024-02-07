from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
import requests

# Create your views here.
url="https://techdevinfoblog.pythonanywhere.com/api/Blog"

def index(request):
    try:
        socialmedia = SocialMediaUrl.objects.all()
        mywork = MyWork.objects.all().order_by('-id')[:3]
        cv = MyCV.objects.last()
        response = requests.get(url)
        if response.status_code == 200:
            blog = response.json()
        else:
            blog = None
    except:
        return redirect('error_page')
    context={
        'socialmedia':socialmedia,
        'mywork':mywork,
        'cv':cv,
        'blogs':blog[len(blog)-3:]
    }
    return render(request, 'index.html', context )

def contactSubmit(request):
    try:
        if request.method == 'POST':
            name= request.POST['name']
            email= request.POST['email']
            subject= request.POST['subject']
            message= request.POST['message']
            userinfo = Contact.objects.create(name=name, email=email, subject=subject, message=message)
            userinfo.save()
            messages.success(request,"Thank you for taking the time to reach out.")
    except:
        return redirect('error_page')
    return redirect('home')



def errorPage(request, exception):
    return render(request, '404.html')
