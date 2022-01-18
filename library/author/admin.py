from django.contrib import admin

from .models import Author


class AuthorAdmin(admin.ModelAdmin):
	list_display = ['first_name', 'last_name', 'country', 'books_count']


admin.site.register(Author, AuthorAdmin)
