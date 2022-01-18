from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# API_TITLE = 'Online Library API Documentation'
# API_DESCRIPTION = 'Online Library where Scholars and anyone can borrow and return books when done'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('author.urls')),
    path('', include('books.urls')),
    path('auth/', include('rest_framework.urls')),
    path('rest/', include('rest_auth.urls')),
    path('rest/reg/', include('rest_auth.registration.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
