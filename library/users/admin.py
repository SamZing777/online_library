from django.contrib import admin

from .models import User


class UserAdmin(admin.ModelAdmin):
	list_display = ['username', 'is_active', 'date_joined']


admin.site.register(User, UserAdmin)



"""
	Admin
	admin@library.com
	libraryAdmin
"""
