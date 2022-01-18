from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import AuthorViewSet
from publisher.views import PublisherViewSet
from users.views import UserViewSet


router = DefaultRouter()
router.register('authors', AuthorViewSet),
router.register('publisher', PublisherViewSet),
router.register('users', UserViewSet)


urlpatterns = [
	path('', include(router.urls)),	
]
