from django.http import Http404

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics

from todoListApp.models import ToDoItem as ToDoItemModel
from todoListApp.models import ToDoList as ToDoListModel
from todoListApp.serializers import ToDoItemSerializer,  ToDoListSerializer


# class based view using the APIView base class
class ToDoItemList(generics.ListCreateAPIView):
    queryset=ToDoItemModel.objects.all()
    serializer_class=ToDoItemSerializer

# class based view using the generics mixins-ready base class for create,update,and delete an item
class ToDoItem(generics.RetrieveUpdateDestroyAPIView):
    queryset=ToDoItemModel.objects.all()
    serializer_class=ToDoItemSerializer


class ToDoLists(generics.ListCreateAPIView):
    queryset=ToDoListModel.objects.all()
    serializer_class=ToDoListSerializer

class ToDoList(generics.RetrieveUpdateDestroyAPIView):
    queryset=ToDoListModel.objects.all()
    serializer_class=ToDoListSerializer
