from rest_framework import serializers

from habits.models import Habit
from habits.validators import *


class HabitSerializer(serializers.ModelSerializer):
    validators = [
        DurationValidator(field='duration'),
        RelatedHabitAndRewardValidator(field1='related_habit', field2='reward'),
        IsPleasantValidator(field1='is_pleasant', field2='related_habit', field3='reward')
    ]

    class Meta:
        model = Habit
        fields = '__all__'
        extra_kwargs = {
            'user': {'required': False}
        }
