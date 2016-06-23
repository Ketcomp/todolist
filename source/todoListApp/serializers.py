from rest_framework import serializers
from todoListApp.models import ToDoItem, ToDoList

class ToDoItemSerializer(serializers.ModelSerializer):
    class Meta:
        model=ToDoItem
        fields = ('title', 'color', 'status', 'due_date', 'parent_list', 'created_date', 'modified_date')


class ToDoListSerializer(serializers.ModelSerializer):
    list_items = serializers.SerializerMethodField()

    class Meta:
        model=ToDoList
        fields = '__all__'

    def get_list_items(self, listObj):
        items=ToDoItem.objects.filter(parent_list=listObj.id)
        items=map(lambda x:ToDoItemSerializer(x).data, items)
        return items



