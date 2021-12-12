from .models import MyUser
from .serializers import UserSerializer
from rest_framework import viewsets, status
from rest_framework.permissions import IsAdminUser
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404, reverse


class UserViewSet(viewsets.ModelViewSet):
    queryset = MyUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]


def verify(request, uuid):
    try:
        user = MyUser.objects.get(verification_uuid=uuid, is_verified=False)
    except MyUser.DoesNotExist:
        raise Http404("User does not exist or is already verified")

    user.is_verified = True
    user.save()
    return redirect('/')
