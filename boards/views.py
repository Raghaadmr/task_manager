from django.shortcuts import render
from .serializers import RigesterSerializer, CreateBoardSerializer, ListBoardSerializer, AddTaskSerializer ,ListTaskSerializer
from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView, DestroyAPIView, CreateAPIView
from rest_framework.permissions import  IsAuthenticated, IsAdminUser ,AllowAny
from .permissions import BoardOwner, BoardOwnertask
from .models import Board, Task
from rest_framework.filters import OrderingFilter


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

class TaskList(ListAPIView):# list for owner

    #queryset = Task.objects.all()
    queryset = Task.objects.filter(is_hidden=True)
    permission_classes = [IsAuthenticated, BoardOwner]
    serializer_class = ListTaskSerializer #list for owner
    filter_backends = [OrderingFilter,]


class TaskListOtherUser(ListAPIView):# list for other user

    queryset = Task.objects.filter(is_hidden=False)# mean not set hidden
    permission_classes = [AllowAny]
    serializer_class = AddTaskSerializer



class AddTask(CreateAPIView):
    permission_classes = [IsAuthenticated, BoardOwner]
    serializer_class = AddTaskSerializer

    def perform_create(self, serializer):
        serializer.save(board_id=self.kwargs['board_id'])


class DeleteBoard(DestroyAPIView):
    queryset = Board.objects.all()
    lookup_field = 'id'
    lookup_url_kwarg = 'board_id'
    serializer_class = ListBoardSerializer
    permission_classes = [IsAuthenticated, BoardOwner ]


class DeleteTask(DestroyAPIView):
    queryset = Task.objects.all()
    lookup_field = 'id'
    lookup_url_kwarg = 'task_id'
    serializer_class = AddTaskSerializer
    permission_classes = [IsAuthenticated, BoardOwnertask]
