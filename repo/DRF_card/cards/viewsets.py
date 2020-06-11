from rest_framework import viewsets
from .models import Cards
from .serializers import CardsSerializer
from rest_framework.pagination import CursorPagination
from .permissions import IsCardsOwner
from rest_framework.permissions import IsAuthenticated

class CustomPagination(CursorPagination):
    ordering = '-id'

class CardsViewSet(viewsets.ModelViewSet):
    queryset = Cards.objects.all()
    serializer_class = CardsSerializer
    pagination_class = CustomPagination
    permission_classes = [IsCardsOwner,]