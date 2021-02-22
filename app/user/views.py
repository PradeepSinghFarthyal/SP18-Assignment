from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import *


# Create your views here.

# class Register_Employee_Api(generics.CreateAPIView):
# queryset = Employee.objects.all()
# serializer_class = RegisterEmployeeSerializer

# Register Employee
class Generate_Unique_Token(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = GenerateUniqueTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        print("Token Generated Successfully", flush=True)
        return Response({'success': 'True', 'token': serializer.data.get('generated_token')}, status=status.HTTP_200_OK)


class Assign_Unique_Token(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = AssignUniqueTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        print("Token Assigned Successfully", flush=True)
        return Response({'success': 'True', 'token': serializer.data.get('assigned_token')}, status=status.HTTP_200_OK)


class Unblock_Unique_Token(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = UnblockUniqueTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        print("Token Unblock Successfully", flush=True)
        return Response({'success': 'True', 'token': serializer.data.get('assigned_token'), 'message': 'Token Unblock successfully'}, status=status.HTTP_200_OK)


class Delete_Unique_Token(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = DeleteTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        print("Token Delete Successfully", flush=True)
        return Response({'success': 'True', 'message': 'Token Delete successfully'}, status=status.HTTP_200_OK)


class Token_Alive(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = TokenAliveSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        print("Token Alive Successfully", flush=True)
        return Response({'success': 'True', 'alive_tokens': serializer.data.get('assigned_token')}, status=status.HTTP_200_OK)

# # Update Employee details
# class Employee_Update_Api(APIView):
#     permission_classes = (AllowAny,)

#     def put(self, request):
#         serializer = EmployeeUpdateApiSerializer(data=request.data, context={'request': request})
#         serializer.is_valid(raise_exception=True)
#         print("Employee data Update Successfully", flush=True)
#         return Response({'success': 'True', 'message': 'Employee Data Update Successfully'}, status=status.HTTP_200_OK)


# # Delete Employee
# class Delete_Employee_Api(APIView):
#     permission_classes = (AllowAny,)

#     def delete(self, request):
#         serializer = DeleteEmployeeApiSerializer(data=request.data, context={'request': request})
#         serializer.is_valid(raise_exception=True)
#         print("Employee data Update Successfully", flush=True)
#         return Response({'success': 'True', 'message': 'Employee Data Update Successfully'}, status=status.HTTP_200_OK)


# # Create Manager
# class Create_Manager(APIView):
#     permission_classes = (AllowAny, )

#     def post(self, request):
#         serializer = CreateManagerSerializer(data=request.data, context={'request': request})
#         serializer.is_valid(raise_exception=True)
#         print("Manager Added Successfully", flush=True)
#         return Response({'success': 'True', 'message': 'Manager Added Successfully'}, status=status.HTTP_200_OK)


# # Allot Manager to Employee
# class Allot_Manager_To_Employee(APIView):
#     permission_classes = (AllowAny, )

#     def post(self, request):
#         serializer = AllotManagerToEmployeeSerializer(data=request.data, context={'request': request})
#         serializer.is_valid(raise_exception=True)
#         print("Manager Added Successfully to Employee", flush=True)
#         return Response({'success': 'True', 'message': 'Manager Added Successfully'}, status=status.HTTP_200_OK)
