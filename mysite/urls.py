from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("polls/", include("polls.urls")),
    path("__debug__/", include("debug_toolbar.urls")),
    path("admin/", admin.site.urls),
]