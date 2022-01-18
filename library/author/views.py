from rest_framework import viewsets, permissions

from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework.response import Response

from .models import Author

from .serializers import (
	AuthorSerializer
	)

from .permissions import IsStaffOrReadOnly


class AuthorViewSet(viewsets.ModelViewSet):
	queryset = Author.objects.all()
	serializer_class = AuthorSerializer
	permission_classes = [IsStaffOrReadOnly, permissions.IsAuthenticatedOrReadOnly]


@api_view(['GET'])
def api_root(request, format=None):
	return Response({
		# 'authors': reverse('authors', request=request, format=format),
		'publishers': reverse('publishers', request=request, format=format),
		'books': reverse('books', request=request, format=format),
		})
