"""
URL configuration for drf project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
"""
urlpatterns = [
    path('talleres/', views.listar_talleres, name='listar_talleres'),
]


def vista_raiz(request):
    return render(request, 'index.html')

urlpatterns += [
    re_path(r'^$', RedirectView.as_view(url='/api/v1/', permanent=False)),
]
"""
from django.contrib import admin
from django.urls import path,include
#from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('api.urls'))
    #path('docs/', include_docs_urls(title='Documentacion_API'))
]
