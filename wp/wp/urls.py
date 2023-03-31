"""wp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from catalogo.views import catalogo,camisas,pantalones,jeans,camisetas,bermudas,calzados,blazers,vestidos,otros,cubaveras,buzos
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', catalogo, name="menu"),
    path('camisas/', camisas, name="camisas"),
     path('cubaveras/', cubaveras, name="cubaveras"),
    path('pantalones/', pantalones, name="pantalones"),
    path('jeans/', jeans, name="jeans"),
    path('camisetas/', camisetas, name="camisetas"),
    path('bermudas/', bermudas, name="bermudas"),
    path('calzados/', calzados, name="calzados"),
    path('blazers/', blazers, name="blazers"),
    path('vestidos/', vestidos, name="vestidos"),
    path('otros/', otros, name="otros"),
    path('buzos/', buzos, name="buzos"),
]
