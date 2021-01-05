# from django.shortcuts import render, HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import UserTask
from .serializers import *

from django.contrib.auth.decorators import login_required


# Create your views here.

# @api_view(['GET'])
# def hello_world(request):
#     return Response('Hello World!')


@api_view(['GET'])
def TaskList(request):
    TasksList = UserTask.objects.all()
    serializer = UserTaskSerializers(TasksList, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def CreateTask(request):
    serializer = UserTaskSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def UpdateTask(request, pk):
    task = UserTask.objects.get(id=pk)
    serializer = UserTaskSerializers(instance=task, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def DeleteTask(request, pk):
    task = UserTask.objects.get(id=pk)
    task.delete()

    return Response('Task succsesfully delete!')


@api_view(['GET'])
def TaskDetail(request, pk):
    tasks = UserTask.objects.get(id=pk)
    serializer = UserTaskSerializers(tasks, many=False)
    return Response(serializer.data)
