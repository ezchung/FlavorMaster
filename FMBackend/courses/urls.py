from django.urls import path
from . import views

#POST
urlpatterns = [
    path("course/", views.CourseListCreate.as_view(), name='course-list'),
    path("course/delete/<int:pk>/", views.CourseDelete.as_view(), name="delete-course"),
    path("course/registered/<int:pk>/", views.UserRegisteredCoursesView.as_view(), name="registered-course-list"),
]