from django.contrib import admin
from . models import StudentProfile
from .models import Student_signup
from .models import ContactMessage
from .models import Course
# Register your models here.
admin.site.register(StudentProfile)
admin.site.register(Student_signup)
admin.site.register(ContactMessage)
admin.site.register(Course)