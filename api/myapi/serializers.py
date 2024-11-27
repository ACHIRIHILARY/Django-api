from rest_framework import serializers
from .models import Blockpost

class BlockpostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blockpost
        fields = ["id", "title", "content", "date"]