from rest_framework import routers, serializers, viewsets
from api.models import Employee


class EmployeeSerialize(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Employee
        fields = ('__all__')