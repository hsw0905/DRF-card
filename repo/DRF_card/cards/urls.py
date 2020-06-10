from rest_framework.routers import SimpleRouter
from .viewsets import CardsViewSet

router = SimpleRouter()
router.register('', CardsViewSet, basename='cards')
urlpatterns = router.urls