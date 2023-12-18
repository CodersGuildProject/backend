from django.urls import path

from . import views

urlpatterns = [
    path("problemlist/",views.problemlist)
]