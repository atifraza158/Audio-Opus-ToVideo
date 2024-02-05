from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from . views import *

urlpatterns = [
    path('', home_page, name='home'),
    path('is_loading/', get_loading, name='get_loading'),
]



urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)