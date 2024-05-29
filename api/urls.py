from django.urls import path, include
from rest_framework import routers
from api import views
from django.shortcuts import render
from django.urls import re_path
from django.views.generic.base import RedirectView

router = routers.DefaultRouter()
router.register(r'Talleres', views.TalleresViewSets)

urlpatterns = [
    path('', include(router.urls))
]



