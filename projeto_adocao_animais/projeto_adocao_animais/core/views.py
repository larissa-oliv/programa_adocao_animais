from django.shortcuts import render
from rest_framework import viewsets
from .models import Abrigo, Animal, Adotante, Agendamento, Mensagem, Doacao, Adocao
from .serializers import AbrigoSerializer, AnimalSerializer, AdotanteSerializer, AgendamentoSerializer, MensagemSerializer, DoacaoSerializer, AdocaoSerializer

class AbrigoViewSet(viewsets.ModelViewSet):
    queryset = Abrigo.objects.all()
    serializer_class = AbrigoSerializer

class AnimalViewSet(viewsets.ModelViewSet):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer

class AdotanteViewSet(viewsets.ModelViewSet):
    queryset = Adotante.objects.all()
    serializer_class = AdotanteSerializer

class AgendamentoViewSet(viewsets.ModelViewSet):
    queryset = Agendamento.objects.all()
    serializer_class = AgendamentoSerializer

class MensagemViewSet(viewsets.ModelViewSet):
    queryset = Mensagem.objects.all()
    serializer_class = MensagemSerializer

class DoacaoViewSet(viewsets.ModelViewSet):
    queryset = Doacao.objects.all()
    serializer_class = DoacaoSerializer

class AdocaoViewSet(viewsets.ModelViewSet):
    queryset = Adocao.objects.all()
    serializer_class = AdocaoSerializer
