"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from qfactor.views import IndexView, Page2View, parse_data 
from rest_framework import routers
from django.views.decorators.csrf import csrf_exempt

router = routers.DefaultRouter()


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(),name='index'),
    path('page2/', csrf_exempt(Page2View.as_view()), name='page2'),
    path('router/', include(router.urls)),
    path('parsedata', parse_data,name='parse_data'),
]
