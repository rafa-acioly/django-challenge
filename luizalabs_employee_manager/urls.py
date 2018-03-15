from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers, serializers, viewsets
from api.models import Employee
import viewsets

router = routers.DefaultRouter()
router.register(r'employee', viewsets.EmployeeViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^admin/', admin.site.urls),
]
