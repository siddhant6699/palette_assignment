from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from .models import Todo
from .serializers import TodoSerializer


class TodoListView(generics.ListCreateAPIView):

    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save()
