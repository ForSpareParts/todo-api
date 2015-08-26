from django.contrib.auth import get_user_model
from rest_framework.viewsets import ModelViewSet

from base import models, serializers

TRUTHY_VALUES = ['1', 'true', 'True']
FALSY_VALUES = ['0', 'false', 'False']


class UserViewSet(ModelViewSet):
    serializer_class = serializers.UserSerializer
    queryset = get_user_model().objects.all()


class ToDoViewSet(ModelViewSet):

    def filter_queryset(self, queryset):

        # process the is_completed filter
        is_completed = self.request.GET.get('is_completed', None)

        if is_completed in TRUTHY_VALUES:
            queryset = queryset.exclude(completed_on=None)
        elif is_completed in FALSY_VALUES:
            queryset = queryset.filter(completed_on=None)


        # hand off the queryset to the normal filtering system
        return super(ModelViewSet, self).filter_queryset(queryset)

    serializer_class = serializers.ToDoSerializer
    queryset = models.ToDo.objects.all()
    filter_fields = ('user',)
