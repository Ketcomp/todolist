# from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection
import json


def index(request):
    return HttpResponse("Test index view")


def db_test(request):
    result = None
    with connection.cursor() as c:
        c.execute("select * from test")
        result = c.fetchall()
    return HttpResponse(json.dumps(result))
