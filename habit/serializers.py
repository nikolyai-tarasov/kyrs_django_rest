from rest_framework import serializers

from habit.models import Habits
from habit.validators import HabitsDurationValidator, HabitsPeriodicityValidator


class HabitSerializer(serializers.ModelSerializer):
    validators = [
        HabitsDurationValidator(field="duration"),
        HabitsPeriodicityValidator(field="periodicity"),
    ]

    class Meta:
        model = Habits
        fields = "__all__"

    def validate(self, data):
        if data.get("related") and data.get("prize"):
            raise serializers.ValidationError(
                "Может быть либо связанная привычка либо вознаграждение,"
            )

        if data.get("is_nice"):
            if data.get("related") or data.get("prize"):
                print("CHECK 1 ser log")
                raise serializers.ValidationError(
                    "У приятной привычки не может быть связанной привычки или "
                    "вознаграждения"
                )

        if data.get("related") and (not data.get("related").is_nice):
            raise serializers.ValidationError("Связанные привычки = приятные привычки")
        return data
