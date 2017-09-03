"""coding_assessment URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from coding_assessment_app import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # Default home page
    url(r'^$', views.index, name='index'),
    # To get list with filter or without fileter
    url(r'search/$', views.appointment_list_all_filter, name='appointment_list_all_filter'),
    # To get the form for creating new entry to scheduler
    url(r'^create/$', views.appointment_save, name='appointment_save'),
]
