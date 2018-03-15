# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
import requests
import pytest
import json
from luizalabs_employee_manager.viewsets import EmployeeViewSet

@pytest.fixture
def temporary_employee():
    from api.models import Employee

    employee = Employee(
        name="Funcionario",
        email="meu_email@gmail.com",
        department="TI")
    employee.save()

    return employee

@pytest.mark.django_db
def test_mount_viewset(temporary_employee):
    viewset = EmployeeViewSet()

    for record_dict in viewset.queryset.values():
        found = True if record_dict['name'] == "Funcionario" else False

    assert found is True

@pytest.mark.django_db
def test_blank_email(client, temporary_employee):
    from api.models import Employee

    response = client.post('/employee/',
                            json.dumps({"name": "Funcionado sem email", "department": "TI"}),
                            HTTP_X_METHOD_OVERRIDE='POST',
                            content_type='application/json')

    assert response.status_code == 400

@pytest.mark.django_db
def test_unique_email(client, temporary_employee):
    from api.models import Employee

    response = client.post('/employee/',
                            json.dumps({"name": "Funcionado email repetido", "department": "TI", "email": "meu_email@gmail.com"}),
                            HTTP_X_METHOD_OVERRIDE='POST',
                            content_type='application/json')
    
    assert response.status_code == 400

@pytest.mark.django_db
def test_update(client, temporary_employee):
    from api.models import Employee

    response = client.post('/employee/{}/'.format(temporary_employee.id),
                           json.dumps({"name": "Funcionario Alterado", "email": "email@email.com", "department": "TI"}),
                           HTTP_X_METHOD_OVERRIDE='PUT',
                           content_type='application/json')

    found_employee = Employee.objects.filter(name="Funcionario")

    assert "Funcionario" not in found_employee

@pytest.mark.django_db
def test_delete(client, temporary_employee):
    from api.models import Employee

    response = client.post('/employee/{}/'.format(temporary_employee.id),
                           json.dumps({"id": temporary_employee.id}),
                           HTTP_X_METHOD_OVERRIDE='DELETE',
                           content_type='application/json')

    found_employee = Employee.objects.filter(name="Funcionario")

    assert "Funcionario" not in found_employee


@pytest.mark.django_db
def test_get(client, temporary_employee):
    response = client.get('/employee/{}/'.format(temporary_employee.id))
    assert response.status_code == 200


@pytest.mark.django_db
def test_get_not_found(client, temporary_employee):
    response = client.get('/employee/46545456/')
    assert response.status_code == 404