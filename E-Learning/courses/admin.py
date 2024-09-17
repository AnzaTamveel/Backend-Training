from django.contrib import admin
from .models import Course, Instructor, Testimonial, Category

admin.site.register(Course)
admin.site.register(Instructor)
admin.site.register(Category)
admin.site.register(Testimonial)
