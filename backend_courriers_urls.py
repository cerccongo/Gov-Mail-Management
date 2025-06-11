from rest_framework.routers import DefaultRouter
from .views import CourrierEntrantViewSet, CourrierSortantViewSet, PieceJointeViewSet

router = DefaultRouter()
router.register("entrants", CourrierEntrantViewSet)
router.register("sortants", CourrierSortantViewSet)
router.register("piecesjointes", PieceJointeViewSet)

urlpatterns = router.urls