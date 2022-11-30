from rest_framework import serializers

from .models import Art, Museum

class ArtSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Art

class MuseumSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Art