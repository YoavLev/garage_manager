from django.db import models
from django.utils import timezone
from django.urls import reverse


# Create your models here.

class Lesson(models.Model):
    date_time = models.DateTimeField(default=timezone.now)
    max_people = models.IntegerField()

    def __str__(self):
        return "Lesson at:{date}".format(date=self.date_time)

    def get_absolute_url(self):
        return reverse('lesson-details', kwargs={'pk': self.pk})


class Person(models.Model):
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    phone_number = models.IntegerField()
    lessons = models.ManyToManyField(Lesson)

    def __str__(self):
        return self.first_name
