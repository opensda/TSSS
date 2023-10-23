from rest_framework import generics

from habits.models import Habit
from habits.paginators import HabitPaginator
from habits.permissions import IsOwner
from habits.serializers import HabitSerializer


class HabitCreateAPIView(generics.CreateAPIView):
    serializer_class = HabitSerializer


class HabitListAPIView(generics.ListAPIView):
    serializer_class = HabitSerializer
    pagination_class = HabitPaginator
    permission_classes = [IsOwner,]


class HabitPublicListAPIView(generics.ListCreateAPIView):
    serializer_class = HabitSerializer
    pagination_class = HabitPaginator
    queryset = Habit.objects.filter(is_public=True)
