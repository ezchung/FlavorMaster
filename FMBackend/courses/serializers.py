from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Course, Registration

#creating serailizers that takes User object into convertable code (JSON)
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password"]
        extra_kwangs = {"password":{"write-only":True}}
    
    def create(self, validated_data):
        # print(validated_data)
        user = User.objects.create_user(**validated_data)
        return user 

    '''Takes data that is already validated from class Meta fields
        Then creates new User
    '''
    def get_registered_courses(self, obj):
        registrations = Registration.objects.filter(user=obj)
        courses = [registration.class_registered for registration in registrations]
        return CourseSerializer(courses, many=True).data
    
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ["id", "title", "description", "created_at", "instructor", "course_date"]
        extra_kwargs = {"instructor": {"read_only": True}} #able to read but not write who author is

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields = ["id", "user", "class_registered", "registration_date"]