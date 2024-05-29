from django.urls import path, include
from rest_framework import routers
from api import views
from django.shortcuts import render
from django.urls import re_path
from django.views.generic.base import RedirectView

router = routers.DefaultRouter()
router.register(r'Talleres', views.TalleresViewSets)

urlpatterns = [
    path('talleres/', views.listar_talleres, name='listar_talleres'),
]

def vista_raiz(request):
    return render(request, 'index.html')

urlpatterns += [
    re_path(r'^$', RedirectView.as_view(url='/api/v1/', permanent=False)),
]