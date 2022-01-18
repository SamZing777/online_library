from rest_framework import viewsets

from .models import Publisher
from .serializers import PublisherSerializer
from author.permissions import IsStaffOrReadOnly


class PublisherViewSet(viewsets.ModelViewSet):
	queryset = Publisher.objects.all()
	serializer_class = PublisherSerializer
	permission_classes = [IsStaffOrReadOnly, ]
