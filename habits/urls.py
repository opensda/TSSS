from django.urls import path

from habits.views import *

urlpatterns = [
    path('create/', HabitCreateAPIView.as_view(), name='habits-create'),
    path('', HabitListAPIView(), name='habits-list'),
    path('public/', HabitPublicListAPIView.as_view(), name='habits-public-list'),
    path('update/<int:pk>/', HabitUpdateAPIView.as_view(), name='habits-update'),
    path('delete/<int:pk>/', HabitDestroyAPIView.as_view(), name='habits-delete'),
]
