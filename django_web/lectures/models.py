from django.db import models
from django.urls import reverse

# Create your models here.
class Lecture(models.Model):
    department = models.CharField(max_length=255, null=True, blank=True)
    number = models.CharField(max_length=255, null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    teacher = models.CharField(max_length=255, null=True, blank=True)
    time_and_room = models.CharField(max_length=255, null=True, blank=True)
    remark = models.CharField(max_length=255, null=True, blank=True)

    def get_absolute_url(self):
        return reverse("lectures:lecture_detail", kwargs={"id": self.id})
