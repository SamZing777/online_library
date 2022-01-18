from rest_framework import viewsets, permissions
from django.contrib.auth import get_user_model

from .serializers import UserSerializer
from .permissions import IsOwnerOrReadOnly

User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer
	permission_classes = [IsOwnerOrReadOnly, ]
