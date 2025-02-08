from django.urls import path

from habit.apps import HabitConfig
from habit.views import (
    HabitsListAPIView,
    HabitsRetrieveAPIView,
    HabitsCreateAPIView,
    HabitsUpdateAPIView,
    HabitsDestroyAPIView,
    HabitsPublicListAPIView,
)

app_name = HabitConfig.name

urlpatterns = [
    path("habits/", HabitsListAPIView.as_view(), name="habits_list"),
    path("habits/<int:pk>/", HabitsRetrieveAPIView.as_view(), name="habits_retrieve"),
    path("habits/create/", HabitsCreateAPIView.as_view(), name="habits_create"),
    path(
        "habits/<int:pk>/update/", HabitsUpdateAPIView.as_view(), name="habits_update"
    ),
    path(
        "habits/<int:pk>/delete/", HabitsDestroyAPIView.as_view(), name="habits_delete"
    ),
    path("public/", HabitsPublicListAPIView.as_view(), name="public_list"),
]
