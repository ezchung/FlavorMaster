from django.db import models
# from instructors.models import Instructor

from django.contrib.auth.models import User
import uuid

# Create your models here.
#Connecting Auth Routes
class Course(models.Model):
    uuid = models.UUIDField(unique=True, default=uuid.uuid4)
    # instructors = models.ManyToManyField(Instructor)
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    instructor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="instructorName")
    date = models.DateTimeField()
    size = models.BigIntegerField()
    #id as a primary key

    def __str__(self):
        return self.title