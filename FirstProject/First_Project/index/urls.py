from django.urls import path
from .views import *

urlpatterns = [
    path('', homepage, name='home'),
    path('contact/', contact, name='contact'),
    path('about/', about, name='about'),

]
