from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny

from habit.models import Habits
from habit.paginators import CustomPagination
from habit.permissions import IsOwner
from habit.serializers import HabitSerializer


class HabitsCreateAPIView(generics.CreateAPIView):
    """Создание привычки для авторизованного пользователя"""
    serializer_class = HabitSerializer
    queryset = Habits.objects.all()

    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        habit = serializer.save()
        habit.owner = self.request.user
        habit.save()


class HabitsListAPIView(generics.ListAPIView):
    """Отображение привычек авторизованного пользователя"""
    serializer_class = HabitSerializer
    queryset = Habits.objects.all()
    permission_classes = (IsAuthenticated,)
    pagination_class = CustomPagination

    def get_queryset(self):
        queryset = self.queryset.filter(owner=self.request.user)
        return queryset


class HabitsRetrieveAPIView(generics.RetrieveAPIView):
    """Просмотр выбранной привычки пользователя"""
    serializer_class = HabitSerializer
    queryset = Habits.objects.all()
    permission_classes = (IsAuthenticated, IsOwner)


class HabitsUpdateAPIView(generics.UpdateAPIView):
    """Обновление выбранной привычки пользователя"""
    serializer_class = HabitSerializer
    queryset = Habits.objects.all()
    permission_classes = (IsAuthenticated, IsOwner)


class HabitsDestroyAPIView(generics.DestroyAPIView):
    """Удаление выбранной привычки пользователя"""
    serializer_class = HabitSerializer
    queryset = Habits.objects.all()
    permission_classes = (IsAuthenticated, IsOwner)


class HabitsPublicListAPIView(generics.ListAPIView):
    """Список публичных привычек"""
    serializer_class = HabitSerializer
    queryset = Habits.objects.all()
    permission_classes = (AllowAny,)
    pagination_class = CustomPagination

    def get_queryset(self):
        queryset = Habits.objects.filter(is_public=True)
        return queryset