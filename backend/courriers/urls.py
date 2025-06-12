from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import (
    CourrierEntrantViewSet,
    CourrierSortantViewSet,
    PieceJointeViewSet,
    public_add_courrier,
)

router = DefaultRouter()
router.register("entrants", CourrierEntrantViewSet)
router.register("sortants", CourrierSortantViewSet)
router.register("piecesjointes", PieceJointeViewSet)

urlpatterns = router.urls + [
    path("add/", public_add_courrier, name="public_add_courrier"),
]
