from rest_framework import serializers
from sales.models import Client

class ClientSerializer(serializers.Serializer):
    fields = {
        "name",
        "num_doc",
        "address",
        "phone",
    }