from __future__ import unicode_literals
from django_daraja.mpesa import utils
from django.http import HttpResponse, JsonResponse
from django.views.generic import View
from datetime import datetime
from django.shortcuts import render, redirect
from decouple import config
from django_daraja.mpesa.core import MpesaClient
from .models import Customer, Game



# Create your views here.
# Home page
def home(request):
    games = Game.objects.all()
    return render(request, 'ticket.html', {'games': games})

def checkout(request):
    cl = MpesaClient()
    # Use a Safaricom phone number that you have access to, for you to be able to view the prompt.
    phone_number = config('LNM_PHONE_NUMBER')
    amount = 1
    account_reference = 'ABC001'
    transaction_desc = 'STK Push Description'
    callback_url = 'https://api.darajambili.com/express-payment'
    r = cl.stk_push(phone_number, amount, account_reference, transaction_desc, callback_url)
    return JsonResponse(r.response_description, safe=False)

def ticket(request):
    return render(request, 'ticket.html')

def cart(request):
    return render(request, 'cart.html')