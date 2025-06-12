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

from django.shortcuts import render, redirect
from .forms import CourrierForm

def public_add_courrier(request):
    if request.method == "POST":
        form = CourrierForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, "courriers/thanks.html")
    else:
        form = CourrierForm()
    return render(request, "courriers/public_add_courrier.html", {"form": form})
