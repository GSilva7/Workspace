"""workspace URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib.auth.views import LoginView
from django.urls import path, include
from .core import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='index'),
    path('/sagebook', views.sagebook, name='sagebook'),
    path('/cetelembook', views.cetelembook, name='cetelembook'),
    path('/sagebdbook', views.sagebdbook, name='sagebdbook'),
    path('', include('django.contrib.auth.urls')),
    path('registrar/', views.register, name='register'),
    path('gmud/', include('workspace.gmud.urls')),
    path('edit/', views.userupdate, name='useredit'),
    path('password/', views.changepassword, name='changepassword'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
