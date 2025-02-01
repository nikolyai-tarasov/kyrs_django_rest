from rest_framework import serializers


class HabitsPeriodicityValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        periodicity = dict(value).get(self.field)
        if 7 < periodicity or periodicity < 1:
            raise serializers.ValidationError('Привычка должна иметь период повторения от 1 дня до 7 дней.')


class HabitsDurationValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        duration = dict(value).get(self.field)
        if duration > 120:
            raise serializers.ValidationError('Длительность привычки не может быть больше 120 минут')