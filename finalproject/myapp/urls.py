from django.urls import path

from . import views
from .views import profile,about
from .views import my_form_view

urlpatterns = [
    path('',views.index,name='index'),
    path('profile/',profile,name='profile'),
    path('about/',about,name='about'),
    path('workwithus/',my_form_view,name='my-form'),
]