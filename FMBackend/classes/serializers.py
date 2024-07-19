from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Class

#creating serailizers that takes User object into convertable code (JSON)
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password"]
        extra_kwangs = {"password":{"write-only":True}}

    '''Takes data that is already validated from class Meta fields
        Then creates new User
    '''
    def create(self, validated_data):
        # print(validated_data)
        user = User.objects.create_user(**validated_data)
        return user 
    
# class ClassSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Class
#         fields = ["id", "title", "content", "created_at", "chef"]
#         extra_kwargs = {"chef": {"read_only": True}}