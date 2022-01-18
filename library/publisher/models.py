from django.db import models
from django.contrib.auth import get_user_model
from autoslug import AutoSlugField

User = get_user_model()


class Publisher(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
	name = models.CharField(max_length=50)
	slug = AutoSlugField(populate_from='name', always_update=False)
	authors = models.PositiveIntegerField(null=True, blank=True)
	books = models.PositiveIntegerField(null=True, blank=True)
	office_address = models.CharField(max_length=200)
	telephone = models.CharField(max_length=20)
	email = models.EmailField()
	year_created = models.CharField(max_length=5)
	website = models.URLField()

	def __str__(self):
		return self.name

	class Meta:
		ordering = ['name']
