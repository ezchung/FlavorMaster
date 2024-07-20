from .models import Course

class CourseUtils:
    def get_all_courses(self):
        """Retrieve all courses."""
        return Course.objects.all()

    def perform_create(self, serializer, user):
        """Perform create operation for a course."""
        if serializer.is_valid():
            serializer.save(author=user)
        else:
            print(serializer.errors)

    def get_personal_course_set(self, user):
        """Retrieve courses authored by the specified user."""
        return Course.objects.filter(author=user)

# Create a single instance of CourseUtils
course_utils = CourseUtils()
