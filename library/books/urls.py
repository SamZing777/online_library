from django.urls import path, include

from .views import (
	BookList,
	BookDetail,
	ReadBook
	)


urlpatterns = [
	path('books/', BookList.as_view(), name='books'),
	path('books/<slug:slug>/', BookDetail.as_view(), name='detail'),
	path('books/<slug:slug>/read/', ReadBook.as_view(), name='read')
]
