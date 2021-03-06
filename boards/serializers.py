from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Board, Task


class RigesterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'last_name',]

    def create(self, validated_data):
        new_user = User(**validated_data)
        new_user.set_password(new_user.password)
        new_user.save()
        return new_user


class CreateBoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = '__all__'

class ListBoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = '__all__'

class AddTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class ListTaskSerializer(serializers.ModelSerializer):
    task_done = serializers.SerializerMethodField()
    task_not_done = serializers.SerializerMethodField()

    class Meta:
        model = Task
        fields = ['board','task_done','task_not_done']
    def get_task_done(self, obj):
        done = Task.objects.filter(is_done= True)
        return AddTaskSerializer(done, many=True).data
    def get_task_not_done(self, obj):
        not_done = Task.objects.filter(is_done= False)
        return AddTaskSerializer(not_done, many=True).data

class HiddenTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['is_hidden']
