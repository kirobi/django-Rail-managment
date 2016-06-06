from django.shortcuts import render, render_to_response, get_object_or_404
from django import http
from .models import Train
from .models import Invoice
from django.contrib import auth
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm

import logging
logger = logging.getLogger(__name__)


def index(request):
    try:
        return render(request, 'index.html')
    except Exception as e:
        logger.error('Problems with rendering index.html: ' + str(e))


def login(request):
    try:
        if request.user.is_authenticated():
            return http.HttpResponseRedirect("/cabinet/")
        else:
            return render(request, 'login.html')
    except Exception as e:
        logger.error('Problems with rendering login page: ' + str(e))


def login_view(request):
    try:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            auth.login(request, user)
            return http.HttpResponseRedirect("/cabinet/")
        else:
            context = {
                'error': 'Username or password are incorrect'
            }
            return render(request, 'error.html', context)
    except Exception as e:
        logger.error('Problems with loging in user: ' + str(e))


def register(request):
    try:
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                new_user = form.save()
                contex = {
                    "message": "Thank you for registration. Now you can log in"
                }
                return http.HttpResponseRedirect("/login/", contex)
        else:
            return http.HttpResponseRedirect("/register/")
    except Exception as e:
        logger.error('Exception was caught while registration: ' + str(e))


def cabinet(request):
    if request.user.is_authenticated():
        context = {
            'invoices': Invoice.objects.filter(user=request.user),
        }
        return render(request, 'cabinet.html', context)
    else:
        return http.HttpResponseRedirect("/login/")


def trains(request):
    try:
        context={}
        print(request.method)
        if request.method == 'GET' and request.GET.get("cityTo", None):
            #form = TrainGetForm(request.POST)
            fr = request.GET.get("cityFrom", None)
            to = request.GET.get("cityTo", None)
            context = {
                'trains': Train.objects.filter(cityFrom=fr, cityTo=to),
            }
        else:
            context = {
                'trains': Train.objects.all(),
            }
        return render(request, 'listRoutes.html', context)
    except Exception as e:
            logger.error('Problems with getting trains from DB: ' + str(e))


def add_invoice(request):
    try:
        if request.user.is_authenticated():
            n = request.GET.get("train", None)
            tr = Train.objects.get(name=n)
            i = Invoice(user=request.user, train=tr, cost=tr.cost+tr.cost*0.2)
            i.save()
            return http.HttpResponseRedirect("/cabinet/")
        else:
            return http.HttpResponseRedirect("/login/")
    except Exception as e:
        logger.error('Problems with creating invoice: ' + str(e))


def pay_invoice(request):
    try:
        if request.user.is_authenticated():
            n = request.GET.get("inv", None)
            Invoice.objects.filter(id=n).update(paid=True)
            return http.HttpResponseRedirect("/cabinet/")
        else:
            return http.HttpResponseRedirect("/login/")
    except Exception as e:
        logger.error('Problems with paying for invoice: ' + str(e))


def logout_view(request):
    try:
        logout(request)
        return http.HttpResponseRedirect("/")
    except Exception as e:
            logger.error('PFailed to logout user. Reason: ' + str(e))

