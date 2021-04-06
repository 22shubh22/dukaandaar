from rest_framework import serializers
from .models import Dukaan, Mal

class DukaanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dukaan
        fields = "__all__"


class MalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mal
        fields = "__all__"