from django.db import models
from django.utils import timezone

from django.contrib.auth.models import User
# Create your models here.
#Connecting Auth Routes
class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    instructor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="instructorName")
    date = models.DateTimeField()
    #id as a primary key

    def __str__(self):
        return self.title

class Registration(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    class_registered = models.ForeignKey(Course, on_delete=models.CASCADE)
    registration_date = models.DateTimeField(auto_now_add=True)
    #id as a primary key

    def __str__(self):
        return f"{self.user.username} - {self.class_registered.title}"

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.user.username

#move each model to individual thing