from rest_framework import viewsets
from .models import Users
from .serializers import UsersSerializer
from rest_framework.pagination import CursorPagination
from .permissions import IsRealUsers
from rest_framework.permissions import IsAuthenticated

class CustomPagination(CursorPagination):
    ordering = '-id'

class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
    pagination_class = CustomPagination
    # permission_classes = [IsAuthenticated, IsRealUsers, ]
    permission_classes = [IsRealUsers, ]