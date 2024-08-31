from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import CourseSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Course
# from .service import get_all_courses
from .service import CourseUtils
course_utils = CourseUtils()



# Create your views here.
#Create Course
class Course(generics.ListCreateAPIView):
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return Response(course_utils.get_all_courses())
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        course_utils.perform_create(serializer, request.user)
        return Response({"message": "Course created successfully"})

    #based on parameters, do certain action
    def get_personal_course_set(self):
        return course_utils.get_personal_course_set(self)
    
    #delete from django
    #

#Deleting courses
class CourseDelete(generics.DestroyAPIView):
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated]

    def get_personal_course_set(self):
        user = self.request.user
        return Course.objects.filter(author=user)
