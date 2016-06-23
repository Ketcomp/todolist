from __future__ import unicode_literals

from datetime import datetime

from django.db import models


class ToDoItem(models.Model):

    OPEN = 0
    COMPLETE = 1
    STATUS_CHOICES = (
        (OPEN, "open"),
        (COMPLETE, "completed" )
    )
    title = models.CharField(max_length=200)
    color = models.CharField(max_length=6)
    status = models.IntegerField(choices=STATUS_CHOICES)
    due_date = models.DateField(default=None, null=True)
    parent_list = models.ForeignKey('ToDoList', on_delete=models.CASCADE)
    created_date = models.DateField(default=datetime.utcnow())
    modified_date = models.DateField(default=datetime.utcnow(),null=True)


class ToDoList(models.Model):
    OPEN = 0
    COMPLETE = 1
    STATUS_CHOICES = (
        (OPEN, "open'"),
        (COMPLETE, "completed" )
    )
    title = models.CharField(max_length=200)
    status = models.IntegerField(choices=STATUS_CHOICES)
    created_date = models.DateField(default=datetime.utcnow())
    modified_date = models.DateField(default=datetime.utcnow(),null=True)
