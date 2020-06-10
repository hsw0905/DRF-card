from rest_framework.routers import SimpleRouter
from .viewsets import UsersViewSet

router = SimpleRouter()
router.register('', UsersViewSet, basename='users')
urlpatterns = router.urls