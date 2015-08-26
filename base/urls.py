from rest_framework.routers import SimpleRouter

from base import api


router = SimpleRouter()

router.register('users', api.UserViewSet)
router.register('to-dos', api.ToDoViewSet)

urlpatterns = router.urls
