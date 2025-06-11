from rest_framework import viewsets
from .models import CourrierEntrant, CourrierSortant, PieceJointe
from .serializers import (
    CourrierEntrantSerializer,
    CourrierSortantSerializer,
    PieceJointeSerializer,
)

class CourrierEntrantViewSet(viewsets.ModelViewSet):
    queryset = CourrierEntrant.objects.all().order_by('-date_reception')
    serializer_class = CourrierEntrantSerializer

class CourrierSortantViewSet(viewsets.ModelViewSet):
    queryset = CourrierSortant.objects.all().order_by('-date_transmission')
    serializer_class = CourrierSortantSerializer

class PieceJointeViewSet(viewsets.ModelViewSet):
    queryset = PieceJointe.objects.all()
    serializer_class = PieceJointeSerializer
