import http.client
from django.shortcuts import render
from django.contrib import messages
from .forms import MyForm


# Create your views here.

def index(request):
    return render(request, 'index.html')


def profile(request):
    return render(request, 'profile.html')


def about(request):
    return render(request, 'about.html')


def my_form_view(request):
    if request.method == "POST":
        form = MyForm(request.POST)
        if form.is_valid():
            form.save()
        messages.success(request, 'Message submitted successfully.')
        form = MyForm()
    else:
        form = MyForm()
    return render (request,'workwithus.html',{'form':form})
