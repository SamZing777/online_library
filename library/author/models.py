from django.db import models
from django.contrib.auth import get_user_model
from autoslug import AutoSlugField
from django_countries.fields import CountryField

User = get_user_model()


class Author(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
	title = models.CharField(max_length=20, null=True, blank=True)
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	slug = AutoSlugField(populate_from='first_name', always_update=False)
	description = models.TextField()
	image = models.ImageField(upload_to='authors')
	country = CountryField(blank_label='(select country)')
	books_count = models.PositiveIntegerField(null=True, blank=True)
	date_of_birth = models.DateField()
	date_of_death = models.DateField(null=True, blank=True)

	def __str__(self):
		return self.first_name

	class Meta:
		ordering = ['first_name']
