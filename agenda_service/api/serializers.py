from rest_framework import serializers
from agenda_service.models import Servico, ExecucaoServico, Feedback

class ServicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servico
        fields = '__all__'

class ExecucaoServicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExecucaoServico
        fields = '__all__'

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'
