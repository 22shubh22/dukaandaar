from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import *
from .models import Dukaan, Mal
from rest_framework.generics import CreateAPIView, RetrieveAPIView, UpdateAPIView, ListAPIView, DestroyAPIView
from rest_framework.response import Response
from django.db import transaction
from rest_framework import status

class CreateDukaanAPI(CreateAPIView):
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

class DukaaanUpdateAPI(UpdateAPIView):
    """
    Dukaan Update API
        Authentication Required: Yes
        Data:
        {
            "dukaan_name": "keycube1",
            "contact_no" : "7780923457",
            "address": "Beldagi",
            "active_status": 0
        }
    """
    serializer_class = DukaanUpdateSerializer
    queryset = Dukaan.objects.all()
    # permission_classes = [permissions.IsAuthenticated]

class CreateMalAPI(CreateAPIView):
    """
    API endpoint that allows groups to be viewed or edited.
    Data:
        {
            "name": "product_name",
            "description" : "product_description",
            "dukaan" : 1,
            "quantity": "1",
            "photo_link" : "will_be_max_upto_four",
            "selling_price" : "500"
        }
    """
    queryset = Mal.objects.all()
    serializer_class = MalSerializer
    # permission_classes = [permissions.IsAuthenticated]

class MalRetrievalAPI(RetrieveAPIView):
    """
    Mal Retrieval GET API
        Service usage and description : This API is used to retrieve kagibase users.
        Authentication Required : YES
    """

    # TODO: add permissions
    serializer_class = MalSerializer
    queryset = Mal.objects.all()

class MalUpdateAPI(UpdateAPIView):
    """
    Mal Update API
        Authentication Required: Yes
        Data:
        {
            "name": "jeans",
            "description" : "Ladies Jeans",
            "quantity": "1"
            "photo_link": "Image link"
            "selling_price": "1000"
        }
    """

    # TODO: permissions
    serializer_class = MalUpdateSerializer
    queryset = Mal.objects.all()

class MalDeleteAPI (DestroyAPIView):
    """
    Mal Delete API
    """
    serializer_class = MalSerializer
    queryset = Mal.objects.all()
