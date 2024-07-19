from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer, CourseSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Course, Registration

# Create your views here.
#Create Course
class CourseListCreate(generics.ListCreateAPIView):
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Course.objects.filter()
    
    def perform_create(self,serializer):
        if serializer.is_valid():
            serializer.save(author=self.request.user)
        else:
            print(serializer.errors)

    def get_personal_course_set(self):
        user = self.request.user
        return Course.objects.filter(author=user)

#Deleting courses
class CourseDelete(generics.DestroyAPIView):
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated]

    def get_personal_course_set(self):
        user = self.request.user
        return Course.objects.filter(author=user)


class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny] #answers who can actually call this

'''
    Get list of courses you registered 
    will need to add user preferences and saved courses to database and 
'''
class UserRegisteredCoursesView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = request.user
        registrations = Registration.objects.filter(user=user)
        courses = [registration.class_registered for registration in registrations]
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)