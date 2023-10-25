from rest_framework.exceptions import ValidationError


class DurationValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        field_value = dict(value).get(self.field)
        if field_value is not None:
            if int(field_value) > 120:
                raise ValidationError('Время выполнения должно быть не больше 120 секунд.')


class RelatedHabitAndRewardValidator:
    def __init__(self, field1, field2):
        self.field1 = field1
        self.field2 = field2

    def __call__(self, value):
        related_habit = dict(value).get(self.field1)
        reward = dict(value).get(self.field2)

        if related_habit and reward:
            raise ValidationError(f"Нельзя одновременно указать {self.field1} и {self.field2}.")


class IsPleasantValidator:
    def __init__(self, field1, field2, field3):
        self.field1 = field1
        self.field2 = field2
        self.field3 = field3

    def __call__(self, value):
        is_pleasant = dict(value).get(self.field1)
        related_habit = dict(value).get(self.field2)
        reward = dict(value).get(self.field3)

        if is_pleasant and (related_habit or reward):
            raise ValidationError("Приятная привычка не может иметь связанной привычки или вознаграждения.")
