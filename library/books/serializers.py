from rest_framework import serializers

from .models import Book


class BookSerializer(serializers.ModelSerializer):

	class Meta:
		model = Book
		fields = '__all__'


"""
class BookSerializer(serializers.HyperlinkedModelSerializer):
	# file = serializers.HyperlinkedIdentityField(view_name='read-book', format='html')

	class Meta:
		model = Book
		fields = ['url', 'id', 'title', 'slug', 'author', 'initial_release', 'cover_image',
		         'pages', 'edition', 'publisher', 'isbn', 'file', 'main_language', 'genre',
		         'Department', 'date_posted', 'reads']
"""
