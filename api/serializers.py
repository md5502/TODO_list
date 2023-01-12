from rest_framework.serializers import ModelSerializer, SerializerMethodField
from todolist.models import Goal, Work


class WorkSerializer(ModelSerializer):
    class Meta:
        model = Work
        fields = '__all__'


class GoalSerializer(ModelSerializer):
    class Meta:
        model = Goal
        fields = '__all__'