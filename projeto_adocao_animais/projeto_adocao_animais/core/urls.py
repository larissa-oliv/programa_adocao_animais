from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AbrigoViewSet, AnimalViewSet, AdotanteViewSet, AgendamentoViewSet, MensagemViewSet, DoacaoViewSet, AdocaoViewSet

router = DefaultRouter()
router.register(r'abrigos', AbrigoViewSet)
router.register(r'animais', AnimalViewSet)
router.register(r'adotantes', AdotanteViewSet)
router.register(r'agendamentos', AgendamentoViewSet)
router.register(r'mensagens', MensagemViewSet)
router.register(r'doacoes', DoacaoViewSet)
router.register(r'adocoes', AdocaoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
