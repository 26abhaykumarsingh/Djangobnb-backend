from rest_framework import serializers

from property.models import Property


class PropertiesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = ["id", "title", "price_per_night", "image_url"]
