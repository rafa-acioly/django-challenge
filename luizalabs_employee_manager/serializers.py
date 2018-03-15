from rest_framework import routers, serializers, viewsets
from api.models import Employee
from rest_framework.validators import UniqueValidator


class EmployeeSerialize(serializers.HyperlinkedModelSerializer):
    read_only_fields = ('created_at')
    email = serializers.EmailField(validators=[UniqueValidator(queryset=Employee.objects.all())])

    class Meta:
        model = Employee
        fields = ('name', 'email', 'department')