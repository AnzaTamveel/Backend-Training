from django.contrib import admin
from .models import Course, Instructor, Testimonial, Category, CustomUser

admin.site.register(Course)
admin.site.register(Instructor)
admin.site.register(Category)
admin.site.register(Testimonial)
admin.site.register(CustomUser)
