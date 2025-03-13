"""
URL configuration for withings_server project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

from rest_framework import routers

from withings import views as withingsviews
 
router = routers.DefaultRouter()


router.register(r'userinfo', withingsviews.UserInfoViewSet)
router.register(r'device', withingsviews.DeviceViewSet)
router.register(r'experiment', withingsviews.ExperimentViewSet)
router.register(r'rawdatarecord', withingsviews.RawdataRecordViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),    
    path("withings_experiments/", withingsviews.withings_experiments),
]
