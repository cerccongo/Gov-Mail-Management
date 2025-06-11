from rest_framework import serializers
from .models import CourrierEntrant, CourrierSortant, PieceJointe

class PieceJointeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PieceJointe
        fields = "__all__"

class CourrierEntrantSerializer(serializers.ModelSerializer):
    pieces_jointes = PieceJointeSerializer(many=True, read_only=True)

    class Meta:
        model = CourrierEntrant
        fields = "__all__"

class CourrierSortantSerializer(serializers.ModelSerializer):
    pieces_jointes = PieceJointeSerializer(many=True, read_only=True)
    lien_courrier_entrant = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = CourrierSortant
        fields = "__all__"