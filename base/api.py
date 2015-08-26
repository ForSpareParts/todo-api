from django.contrib.auth import get_user_model
from rest_framework.viewsets import ModelViewSet

from base import models, serializers


class UserViewSet(ModelViewSet):
    serializer_class = serializers.UserSerializer
    queryset = get_user_model().objects.all()


class ToDoViewSet(ModelViewSet):
    serializer_class = serializers.ToDoSerializer
    queryset = models.ToDo.objects.all()
