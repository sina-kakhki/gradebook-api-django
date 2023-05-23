from gradebook.models import *
from django.contrib import admin

# Register your models here.
admin.site.register(Semester)
admin.site.register(Class)
admin.site.register(Course)
admin.site.register(Student)
admin.site.register(Lecturer)
admin.site.register(StudentEnrollment)
