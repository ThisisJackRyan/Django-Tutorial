from django.contrib import path

from . import views
urlpatterns = [
    path("", views.index, name="index")
]