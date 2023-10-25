from rest_framework import serializers

from habits.models import Habit
from habits.validators import DurationValidator


class HabitSerializer(serializers.ModelSerializer):
    validators = [
        DurationValidator(field='duration'),
    ]

    class Meta:
        model = Habit
        fields = '__all__'
        extra_kwargs = {
            'user': {'required': False}
        }
