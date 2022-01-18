from rest_framework import (
	generics,
	permissions
	)

from rest_framework.response import Response
from drf_pdf.renderer import PDFRenderer

from .models import Book
from .serializers import BookSerializer

from author.permissions import IsStaffOrReadOnly


class BookList(generics.ListAPIView):
	queryset = Book.objects.all()
	serializer_class = BookSerializer


class BookDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Book.objects.all()
	serializer_class = BookSerializer
	lookup_field = 'slug'
	permission_classes = [IsStaffOrReadOnly, ]


class ReadBook(generics.GenericAPIView):
	queryset = Book.objects.all()
	lookup_field = 'slug'
	renderer_classes = [PDFRenderer, ]

	def get(self, request, *args, **kwargs):
		book = self.get_object()
		return Response(
			book.file
		)


"""
class BookViewSet(viewsets.ModelViewSet):
	queryset = Book.objects.all()
	serializer_class = BookSerializer
	permission_classes = [IsStaffOrReadOnly, ]

	@action(detail=True, renderer_classes=[PDFRenderer])
	def the_book(self, request, *args, **kwargs):
		to_read = self.get_object()
		return Response(to_read.file)

	def perform_create(self, serializer):
		serializer.save(user=self.request.user)
"""
