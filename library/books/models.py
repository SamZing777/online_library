from django.db import models
from django.urls import reverse
from autoslug import AutoSlugField
from django.contrib.auth import get_user_model

from author.models import Author
from publisher.models import Publisher

User = get_user_model()


class Genre(models.Model):
	name = models.CharField(max_length=20)

	def __str__(self):
		return self.name

	class Meta:
		ordering = ['name']


class Department(models.Model):
	name = models.CharField(max_length=20)

	def __str__(self):
		return self.name

	class Meta:
		ordering = ['name']


class Book(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
	title = models.CharField(max_length=150)
	slug = AutoSlugField(populate_from='title', always_update=False)
	author = models.ForeignKey(Author, on_delete=models.CASCADE)
	initial_release = models.CharField(max_length=20)
	cover_image = models.ImageField(upload_to='book_cover', default='http://127.0.0.1:8000/media/authors/JKRowling.jpeg')
	pages = models.PositiveIntegerField(null=True, blank=True)
	edition = models.CharField(max_length=20)
	publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
	isbn = models.CharField(max_length=20)
	file = models.FileField(upload_to='files')
	main_language = models.CharField(max_length=40)
	genre = models.ForeignKey(Genre, on_delete=models.CASCADE, null=True, blank=True)
	Department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True, blank=True)
	date_posted = models.DateTimeField(auto_now_add=True)
	reads = models.PositiveIntegerField(null=True, blank=True)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('detail', args=[str(self.slug)])

	class Meta:
		ordering = ['title']
