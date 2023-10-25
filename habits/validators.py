from rest_framework.exceptions import ValidationError


class DurationValidator:

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        field_value = dict(value).get(self.field)
        if field_value is not None:
            if int(field_value) > 120:
                raise ValidationError('Время выполнения должно быть не больше 120 секунд.')
