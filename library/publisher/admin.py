from django.contrib import admin

from .models import Publisher


class PublisherAdmin(admin.ModelAdmin):
	list_display = ['name', 'year_created', 'website']


admin.site.register(Publisher, PublisherAdmin)
