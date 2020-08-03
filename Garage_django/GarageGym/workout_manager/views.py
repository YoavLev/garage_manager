from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Person, Lesson
from .tables import LessonTable
from django.http import HttpResponse
from django_tables2 import SingleTableView
from bootstrap_modal_forms.generic import BSModalCreateView, BSModalDeleteView
from .forms import PersonModelForm
from django.urls import reverse_lazy


# Create your views here.

def home(request):
    return render(request, 'workout_manager/home.html')


# def participants(request):
#     table = LessonTable(Lesson.objects.all())
#
#     return render(request, "workout_manager/lesson-details.html", {
#         "table": table
#     })

class LessonListView(ListView):
    model = Lesson
    template_name = 'workout_manager/lessons_list.html'
    context_object_name = 'lessons'


class LessonDetailView(DetailView):
    model = Lesson


class PersonCreateView(BSModalCreateView):
    template_name = 'workout_manager/join_lesson.html'
    form_class = PersonModelForm
    success_message = 'Success: You joined the workout'
    success_url = reverse_lazy('lessons-list')


class PersonDeleteView(BSModalDeleteView):
    model = Person
    template_name = 'workout_manager/quit_lesson.html'
    success_message = 'Success: You quit the workout.'
    success_url = reverse_lazy('lessons-list')
