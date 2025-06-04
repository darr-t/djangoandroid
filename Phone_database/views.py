from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from Phone_database.models import Student
from Phone_database.serializer import StudentSerializer


# Create your views here.
@api_view(['POST'])
def save(request):
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid(): #valid means it is in the database
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def fetch(request):
    # Student.objects.create(name="Lucy Chen",
    #                        email="chenlucy@gmail.com",
    #                        password="timtest",
    #                        gender="female",
    #                        sports="netball",
    #                        education="university",)
    students = Student.objects.all()
    serializer = StudentSerializer(students, many=True)
    return Response(serializer.data)  #serializer converts to and from JSON...return response returns the data to user who asked for it