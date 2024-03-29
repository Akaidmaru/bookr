from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

import bookr.views
from bookr.views import profile
from django.contrib import admin

# import reviews.views

urlpatterns = [
    path('accounts/', include(('django.contrib.auth.urls', 'auth'), namespace='accounts')),
    path('accounts/profile/', profile, name='profile'),
    path('admin/', admin.site.urls),
    path('', include('reviews.urls')),
    path('filter_demo/', include('filter_demo.urls')),
    path('book_management/', include('book_management.urls')),
    path('accounts/profile/reading_history', bookr.views.reading_history, name='reading_history'),
    path('', include('bookr_test.urls'))

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
