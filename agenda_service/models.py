from django.db import models

class Servico(models.Model):
    nome = models.CharField(max_length=255)
    estimativa_tempo = models.IntegerField()  # em minutos
    def __str__(self):
        return self.nome

class ExecucaoServico(models.Model):
    servico = models.ForeignKey(Servico, on_delete=models.CASCADE)
    tempo_real = models.IntegerField()  # em minutos
    data_execucao = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.servico

class Feedback(models.Model):
    execucao_servico = models.ForeignKey(ExecucaoServico, on_delete=models.CASCADE)
    comentario = models.TextField()
    avaliacao = models.IntegerField()  # pode ser uma escala de 1 a 5
    
    def __str__(self):
        return self.execucao_servico
