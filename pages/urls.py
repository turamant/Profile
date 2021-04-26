from django.urls import path

from pages.views import resume_view, links_view

urlpatterns = [
    path('links/', links_view, name='links'),
    path('resume/', resume_view, name='resume'),
]