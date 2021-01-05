from rest_framework import serializers
from .models import UserTask


class UserTaskSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserTask
        fields = '__all__'
