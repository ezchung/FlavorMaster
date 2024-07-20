from .models import Course

#make a module to import
def get_all_courses(self):
    return Course.objects.all()

def perform_create(self,serializer):
    if serializer.is_valid():
        serializer.save(author=self.request.user)
    else:
        print(serializer.errors)

def get_personal_course_set(self):
    user = self.request.user
    return Course.objects.filter(author=user)