from django.urls import path
from . import views

urlpatterns = [
   path('', views.index, name='index'),
   path('btc.html', views.btc, name='btc'),
   path('contact.html', views.contact, name='contact'),
   path('paypal.html', views.paypal, name='paypal'),
]
