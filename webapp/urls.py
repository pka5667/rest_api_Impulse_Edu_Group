from django.urls import path

from .views import get_assignments, post_assignments

urlpatterns = [
    path("all/", get_assignments, name="get"),
    path("new/", post_assignments, name="post"),
]
