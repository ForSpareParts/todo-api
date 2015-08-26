from django.contrib.auth import get_user_model
from rest_framework.viewsets import ModelViewSet

from base import models, serializers

TRUTHY_VALUES = ['1', 'true', 'True']

class UserViewSet(ModelViewSet):
    serializer_class = serializers.UserSerializer
    queryset = get_user_model().objects.all()


class ToDoViewSet(ModelViewSet):

    def filter_queryset(self, queryset):

        # process the is_completed filter
        if self.request.GET.get('is_completed', None) in TRUTHY_VALUES:
            queryset = queryset.exclude(completed_on=None)


        # hand off the queryset to the normal filtering system
        return super(ModelViewSet, self).filter_queryset(queryset)

    serializer_class = serializers.ToDoSerializer
    queryset = models.ToDo.objects.all()
    filter_fields = ('user',)
