import django_tables2 as tables
from .models import Lesson


class LessonTable(tables.Table):
    class Meta:
        model = Lesson
        template_name = "django_tables2/bootstrap.html"

