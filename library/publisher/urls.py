"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import PublisherList


urlpatterns = [
	path('publishers/', PublisherList.as_view(), name='publishers')
]
"""
