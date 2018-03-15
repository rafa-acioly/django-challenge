from rest_framework import routers, serializers, viewsets
from api.models import Employee


class EmployeeSerialize(serializers.HyperlinkedModelSerializer):
    read_only_fields = ('created_at')

    class Meta:
        model = Employee
        fields = ('name', 'email', 'department')