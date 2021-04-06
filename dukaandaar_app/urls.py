from django.urls import path, include
from .views import *

urlpatterns = [
    path("dukaan/create", DukaanView.as_view()),
    path("mal/", MalView.as_view()),
]