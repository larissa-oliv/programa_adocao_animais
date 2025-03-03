from django.db import models

class Abrigo(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.TextField()
    contato = models.CharField(max_length=100)

class Animal(models.Model):
    nome = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50)
    idade = models.IntegerField()
    raca = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='fotos/')
    abrigo = models.ForeignKey(Abrigo, on_delete=models.CASCADE)

class Adotante(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.TextField()
    contato = models.CharField(max_length=100)
    historico_adocoes = models.ManyToManyField(Animal, through='Adocao')

class Agendamento(models.Model):
    data = models.DateTimeField()
    abrigo = models.ForeignKey(Abrigo, on_delete=models.CASCADE)
    adotante = models.ForeignKey(Adotante, on_delete=models.CASCADE)

class Mensagem(models.Model):
    texto = models.TextField()
    data = models.DateTimeField(auto_now_add=True)
    remetente = models.ForeignKey(Adotante, on_delete=models.CASCADE, related_name='mensagens_enviadas')
    destinatario = models.ForeignKey(Abrigo, on_delete=models.CASCADE, related_name='mensagens_recebidas')

class Doacao(models.Model):
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    metodo_pagamento = models.CharField(max_length=100)
    data = models.DateTimeField(auto_now_add=True)
    adotante = models.ForeignKey(Adotante, on_delete=models.CASCADE)
    abrigo = models.ForeignKey(Abrigo, on_delete=models.CASCADE)

class Adocao(models.Model):
    adotante = models.ForeignKey(Adotante, on_delete=models.CASCADE)
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    data_adocao = models.DateTimeField(auto_now_add=True)
