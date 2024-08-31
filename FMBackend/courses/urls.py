from django.urls import path
from . import views

urlpatterns = [
    path("courses/", views.CourseListCreate.as_view(), name='course-list'),
    # path("courses/personal/",views.PersonalCourseList.as_view())
    path("courses/<int:pk>/delete", views.CourseDelete.as_view(), name="delete-course"), #patch or delete a course
    #how should path work in order for user to select delete rather than add or other options when frontend makes a call
    #when frontend calls, will attach whether delete or add
    path("courses/registered/<int:pk>/", views.UserRegisteredCoursesView.as_view(), name="registered-course-list"),
]

# figure out how to prepare this to be used by frontend
