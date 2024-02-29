from rest_framework import serializers
from agenda_service.models import Servico, ExecucaoServico, Feedback

class ServicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servico
        fields = ['nome','estimativa_tempo']

class ExecucaoServicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExecucaoServico
        fields = ['servico','tempo_real','data_execucao']

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ['execucao_servico','comentario','avaliacao']
