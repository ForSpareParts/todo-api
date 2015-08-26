from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer

from base import models


class UserSerializer(ModelSerializer):

    class Meta:
        fields = ('id', 'username', 'email')
        model = get_user_model()


class ToDoSerializer(ModelSerializer):

    class Meta:
        model = models.ToDo
        fields = ('id', 'title', 'user', 'completed_on')
