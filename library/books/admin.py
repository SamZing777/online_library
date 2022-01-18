from django.contrib import admin

from .models import (
	Genre,
	Department,
	Book
	)


class BookAdmin(admin.ModelAdmin):
	list_display = ['title', 'author', 'main_language', 'genre', 'reads']


admin.site.register(Genre)
admin.site.register(Department)
admin.site.register(Book, BookAdmin)
