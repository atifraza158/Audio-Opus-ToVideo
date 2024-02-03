from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from . views import *

urlpatterns = [
    path('', home_page, name='home'),
    path('success/', success_page, name='success'),
]



urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)