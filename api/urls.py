#from django.urls import path,include
#from rest_framework import routers
#from api import views

#router = routers.DefaultRouter()
#router.register(r'agendamientos', views.AgendamientoViewsets)

#urlpatterns=[
#    path('', include(router.urls))
#]

from django.urls import path
from .views import TalleresList

urlpatterns = [
    path('talleres/', TalleresList.as_view(), name='talleres-list'),
]



from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('talleres.urls')),
]