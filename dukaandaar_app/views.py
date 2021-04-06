from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import DukaanSerializer, MalSerializer
from .models import Dukaan, Mal
from rest_framework.generics import CreateAPIView, RetrieveAPIView, UpdateAPIView, ListAPIView
from rest_framework.response import Response
from django.db import transaction
from rest_framework import status

class DukaanView(CreateAPIView):
    """
    API endpoint that allows users to be viewed or edited.

    Request Data:
    {
        "dukaan_name" : "Shri Laxmi Flour and Oil Mill",
        "password": "1234@test",
        "contact_number": "126457",
        "address": "Lakhanpur"
    }

    Responds with user_id and password default password.

    """
    queryset = Dukaan.objects.all()
    serializer_class = DukaanSerializer
    # permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        try:
            data = request.data
            with transaction.atomic():
                user = User.objects.create(
                    username=data["dukaan_name"], password=data["password"],
                )
                user.set_password(data["password"])
                user.save()

                data["dukaan_id"] = user.id
                serializer = DukaanSerializer(data=data)
                if serializer.is_valid(raise_exception=True):
                    serializer.save()
                    return Response(data=serializer.data, status=status.HTTP_200_OK,)
        except Exception as e:
            transaction.rollback()
            return Response({"message": str(e)}, status=status.HTTP_406_NOT_ACCEPTABLE)


class MalView(CreateAPIView):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Mal.objects.all()
    serializer_class = MalSerializer
    permission_classes = [permissions.IsAuthenticated]