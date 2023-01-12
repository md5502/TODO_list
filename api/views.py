from rest_framework import viewsets
from .serializers import GoalSerializer, WorkSerializer
from todolist.models import Work, Goal
# Create your views here.

class WorkViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Work.objects.all()
    serializer_class = WorkSerializer

class GoalViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Goal.objects.all()
    serializer_class = GoalSerializer