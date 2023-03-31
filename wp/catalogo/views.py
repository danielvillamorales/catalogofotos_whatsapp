from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from django.shortcuts import get_object_or_404, render,redirect
from catalogo.models import *
from django.db.models import Q
from django.conf import settings
from django.contrib.auth.models import User,Permission,ContentType,Group
from django.contrib.auth.decorators import login_required
import datetime
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

def catalogo(request):
    return render(request,'base.html')

def camisas(request):
    referencias= WpDisponibles.objects.filter(grupo='01')
    return render(request,'referencias.html',{'referencias':referencias})

def pantalones(request):
    referencias= WpDisponibles.objects.filter(grupo='02')
    return render(request,'referencias.html',{'referencias':referencias})


def jeans(request):
    referencias= WpDisponibles.objects.filter(grupo='35')
    return render(request,'referencias.html',{'referencias':referencias})


def camisetas(request):
    referencias= WpDisponibles.objects.filter(Q(grupo='03')|Q(grupo='60')|Q(grupo='30'))
    return render(request,'referencias.html',{'referencias':referencias})

def bermudas(request):
    referencias= WpDisponibles.objects.filter(grupo='04')
    return render(request,'referencias.html',{'referencias':referencias})

def calzados(request):
    referencias= WpDisponibles.objects.filter(Q(grupo='10')|Q(grupo='1A')|Q(grupo='1L'))
    return render(request,'referencias.html',{'referencias':referencias})

def blazers(request):
    referencias= WpDisponibles.objects.filter(Q(grupo='21')|Q(grupo='18'))
    return render(request,'referencias.html',{'referencias':referencias})

def vestidos(request):
    referencias= WpDisponibles.objects.filter(grupo='22')
    return render(request,'referencias.html',{'referencias':referencias})

def otros(request):
    referencias= WpDisponibles.objects.filter(Q(grupo='CRR'))
    return render(request,'referencias.html',{'referencias':referencias})

def cubaveras(request):
    referencias= WpDisponibles.objects.filter(Q(subgrupo='0118'))
    return render(request,'referencias.html',{'referencias':referencias})

def buzos(request):
    referencias= WpDisponibles.objects.filter(Q(subgrupo='6003'))
    return render(request,'referencias.html',{'referencias':referencias})