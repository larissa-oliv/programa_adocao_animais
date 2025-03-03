from rest_framework import serializers
from .models import Abrigo, Animal, Adotante, Agendamento, Mensagem, Doacao, Adocao

class AbrigoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Abrigo
        fields = '__all__'

class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = '__all__'

class AdotanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adotante
        fields = '__all__'

class AgendamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agendamento
        fields = '__all__'

class MensagemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mensagem
        fields = '__all__'

class DoacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doacao
        fields = '__all__'

class AdocaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adocao
        fields = '__all__'
