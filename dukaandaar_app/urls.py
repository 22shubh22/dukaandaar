from django.urls import path, include
from .views import *

urlpatterns = [
    path("dukaan/create/", CreateDukaanAPI.as_view()),
    path("dukaan/ud/<int:pk>/", DukaaanUpdateAPI.as_view()),
    path("mal/create/", CreateMalAPI.as_view()),
    path("mal/<int:pk>/", MalRetrievalAPI.as_view()),
    path("mal/ud/<int:pk>/", MalUpdateAPI.as_view()),
    path("mal/delete/<int:pk>/", MalDeleteAPI.as_view()),
]