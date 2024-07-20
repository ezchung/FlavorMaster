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