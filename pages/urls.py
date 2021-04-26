from django.urls import path

from pages.views import resume_view, links_view, PostListView, PostDetailView

urlpatterns = [
    path('links/', links_view, name='links'),
    path('resume/', resume_view, name='resume'),
    path('list/',PostListView.as_view(), name='post_list'),
    path('list/<slug:slug>/',PostDetailView.as_view(), name='post_detail'),
]