from rest_framework.routers import SimpleRouter
from .viewsets import UsersViewSet

router = SimpleRouter(trailing_slash=False)
router.register('', UsersViewSet, basename='users')
urlpatterns = router.urls