
from django.contrib import admin
from django.urls import path, include

from pages.views import base_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',base_view, name='_base'),
    path('pages/',include('pages.urls')),
]
