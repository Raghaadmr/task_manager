from django.shortcuts import render
from .serializers import RigesterSerializer, CreateBoardSerializer, ListBoardSerializer, AddTaskSerializer
from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView, DestroyAPIView, CreateAPIView
from rest_framework.permissions import  IsAuthenticated, IsAdminUser
from .permissions import BoardOwner
from .models import Board, Task


class Rigester(CreateAPIView):
    serializer_class = RigesterSerializer

class BoardCreate(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CreateBoardSerializer
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class BoardList(ListAPIView):
    queryset = Board.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = ListBoardSerializer


class AddTask(CreateAPIView):
    permission_classes = [IsAuthenticated, BoardOwner]
    serializer_class = AddTaskSerializer

    def perform_create(self, serializer):
        serializer.save(board_id=self.kwargs['board_id'])
