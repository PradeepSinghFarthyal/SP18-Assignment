from rest_framework import serializers
from .views import *
from .models import *
from django.conf import settings
import os, base64
import io
import json
import secrets

pool = []
assigned_token_pool = []


class GenerateUniqueTokenSerializer(serializers.Serializer):
    generated_token = serializers.CharField(max_length=255, read_only=True)

    def validate(self, data):
        try:
            token = secrets.token_hex()
            if token not in pool:
                pool.append(token)
        except PermissionError:
            raise serializers.ValidationError('Token Not Generated')
        print("POOL", pool)
        return {"generated_token": token}


class AssignUniqueTokenSerializer(serializers.Serializer):
    assigned_token = serializers.CharField(max_length=255, read_only=True)

    def validate(self, data):
        try:
            if not pool:
                raise serializers.ValidationError('Token not available')
            token = pool.pop()
            assigned_token_pool.append(token)
        except PermissionError:
            raise serializers.ValidationError('Token Not Assigned')
        return {"assigned_token": token}


class UnblockUniqueTokenSerializer(serializers.Serializer):
    token = serializers.CharField(max_length=255, write_only=True)
    assigned_token = serializers.CharField(max_length=255, read_only=True)

    def validate(self, data):
        try:
            tkn = data.get("token", None)
            if tkn in assigned_token_pool:
                pool.append(tkn)
                assigned_token_pool.remove(tkn)
            else:
                raise serializers.ValidationError('Given Token is invalid')
        except PermissionError:
            raise serializers.ValidationError('Token Not Unblocked')
        return {"assigned_token": tkn}


class DeleteTokenSerializer(serializers.Serializer):
    token = serializers.CharField(max_length=255, write_only=True)

    def validate(self, data):
        try:
            tkn = data.get("token", None)
            if tkn in pool:
                pool.remove(tkn)
            elif tkn in assigned_token_pool:
                assigned_token_pool.remove(tkn)
            else:
                raise serializers.ValidationError('This token is not a valid token')
        except PermissionError:
            raise serializers.ValidationError('Token Not Deleted')
        return {"assigned_token": tkn}


class TokenAliveSerializer(serializers.Serializer):
    assigned_token = serializers.ListField(read_only=True)

    def validate(self, data):
        try:
            pool.extend(assigned_token_pool)
        except PermissionError:
            raise serializers.ValidationError('Token Not Alive')
        return {"assigned_token": pool}
# class RegisterEmployeeSerializer(serializers.Serializer):
#     email = serializers.EmailField(max_length=255, write_only=True)
#     emp_name = serializers.CharField(max_length=255, write_only=True)

#     def validate(self, data):
#         email = data.get('email', None)
#         emp_name = data.get('emp_name', None)
#         try:
#             if Employee.objects.filter(email=email).exists():
#                 raise serializers.ValidationError('Email already register. Please try with another email')
#             employee_data = Employee(email=email, emp_name=emp_name)
#             employee_data.save()
#         except PermissionError:
#             raise serializers.ValidationError('Employee Not Added Successfully')
#         return True


# class EmployeeUpdateApiSerializer(serializers.Serializer):
#     id = serializers.IntegerField(write_only=True)
#     emp_name = serializers.CharField(max_length=255, write_only=True)

#     def validate(self, data):
#         id = data.get('id', None)
#         emp_name = data.get('emp_name', None)
#         try:
#             employee_details = Employee.objects.get(id=id)
#             employee_details.emp_name = emp_name
#             employee_details.save()
#         except PermissionError:
#             raise serializers.ValidationError('Data not updated successfully')
#         return True


# class DeleteEmployeeApiSerializer(serializers.Serializer):
#     emp_id = serializers.IntegerField()

#     def validate(self, data):
#         emp_id = data.get('emp_id', None)
#         try:
#             employee_details = Employee.objects.get(id=emp_id)
#             manager_details = employee_details.manger_set.all()
#             if manager_details is not None:
#                 emp_manager = manager_details[0].employee_manager_set.all()
#                 # emp_manager = Employee_Manager.objects.filter(manager_id=manager_details[0].id)
#                 # if emp_manager is not None:
#                 employee_id = [i.emp.id for i in emp_manager]
#             print("employee_id", employee_id)
#             employee_details.delete()
#             for emp in employee_id:
#                 e_m_data = Employee_Manager(emp=Employee.objects.get(id=emp), manager=Manger.objects.get(id=8))
#                 e_m_data.save()
#             print(employee_details)
#         except PermissionError:
#             pass
#         return True


# class CreateManagerSerializer(serializers.Serializer):
#     emp_id = serializers.IntegerField()

#     def validate(self, data):
#         emp_id = data.get('emp_id', None)
#         try:
#             emp_obj = Employee.objects.get(id=emp_id)
#             manager_data = Manger(emp=emp_obj)
#             manager_data.save()
#             print("Manager Added")
#         except PermissionError:
#             raise serializers.ValidationError('Manager Not Added')
#         return True


# class AllotManagerToEmployeeSerializer(serializers.Serializer):
#     emp_id = serializers.IntegerField()
#     manager_id = serializers.IntegerField()

#     def validate(self, data):
#         emp_id = data.get('emp_id', None)
#         manager_id = data.get('manager_id', None)
#         try:
#             final_data = Employee_Manager(emp=Employee.objects.get(id=emp_id), manager=Manger.objects.get(id=manager_id))
#             final_data.save()
#         except PermissionError:
#             raise serializers.ValidationError('Manager Not Allot')
#         return True
