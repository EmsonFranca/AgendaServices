from rest_framework import viewsets
from agenda_service.models import Servico, ExecucaoServico, Feedback
from agenda_service.api.serializers import ServicoSerializer, ExecucaoServicoSerializer, FeedbackSerializer

class ServicoViewSet(viewsets.ModelViewSet):
    queryset = Servico.objects.all()
    serializer_class = ServicoSerializer

class ExecucaoServicoViewSet(viewsets.ModelViewSet):
    queryset = ExecucaoServico.objects.all()
    serializer_class = ExecucaoServicoSerializer

class FeedbackViewSet(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
