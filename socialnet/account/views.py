from __future__ import unicode_literals

from rest_framework import viewsets
from rest_framework import routers

from account.models import User
from account.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


router = routers.DefaultRouter()
router.register('users', UserViewSet)