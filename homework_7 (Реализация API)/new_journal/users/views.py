from .models import MyUser
from .serializers import UserSerializer
from rest_framework import viewsets, status
from rest_framework.permissions import IsAdminUser


class UserViewSet(viewsets.ModelViewSet):
    queryset = MyUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]
