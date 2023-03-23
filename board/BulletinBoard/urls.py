from django.contrib import admin
from django.urls import path, include

from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path("accounts/", include("accounts.urls")),
    path('pages/', include('django.contrib.flatpages.urls')),
    path('tinymce/', include('tinymce.urls')),
    path('', (AdsList.as_view()), name='AdsList'),
    path('<int:pk>', (Ads.as_view()), name='Ads'),
    path('ads/create/', AdsCreate.as_view(), name='Ads_create'),
    path('ads/<int:pk>/edit/', AdsUpdate.as_view(), name='Ads_update'),
]