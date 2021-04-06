from django.urls import path, include
from .views import *

urlpatterns = [
    path("dukaan/create/", CreateDukaanAPI.as_view()),
    path("dukaan/ud/<int:pk>/", DukaaanUpdateAPI.as_view()),
    path("mal/", MalView.as_view()),
]