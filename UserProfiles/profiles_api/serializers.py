from rest_framework import serializers


class HelloSerializer(serializers.Serializer):
    """This is sample serializer class"""

    name = serializers.CharField(max_length=10)
