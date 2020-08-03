from django.urls import path

from . import views

urlpatterns = [
    path('lessons_list/', views.LessonListView.as_view(), name='lessons-list'),
    path('lessons_list/join/', views.PersonCreateView.as_view(), name='join_lesson'),
    path('lessons_list/quit/<int:pk>', views.PersonDeleteView.as_view(), name='quit_lesson'),
    path('lesson-details/<int:pk>/', views.LessonDetailView.as_view(), name='lesson-details'),
    path('', views.home, name='home'),
]