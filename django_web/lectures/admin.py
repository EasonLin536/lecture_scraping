from django.contrib import admin

# Register your models here.
from .models import Lecture

class LectureAdmin(admin.ModelAdmin):
    list_display = ('department', 'number', 'name', 'teacher', 'time_and_room', 'remark')


admin.site.register(Lecture, LectureAdmin)