from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response

from my_first_testapp.controller.dep_controller import adddepartmentcontroller, deletedepartmentController, \
    updatedepartmentController, getbyiddepartmentcontroller, getalldepartmentcontroller
from my_first_testapp.serializer import DepartmenSerializer


@api_view(['POST'])
def adddepartmentview(request):
    response = adddepartmentcontroller(request)
    serializer = DepartmenSerializer(response)
    return Response(serializer.data)


@api_view(['DELETE'])
def deletedepartmentview(request, pk):
    response = deletedepartmentController(request, pk)
    if response is not None:
        return Response('deleted')
    else:
        return HttpResponse('not found')


@api_view(['POST'])
def updatedepartmentview(request, pk):
    response = updatedepartmentController(request, pk)
    serializer = DepartmenSerializer(response)
    return Response(serializer.data)


@api_view(['GET'])
def getbyiddepartmentview(request, pk):
    response = getbyiddepartmentcontroller(request, pk)
    serializer = DepartmenSerializer(response, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def getalldepartmentview(request):
    response = getalldepartmentcontroller(request)
    serializer = DepartmenSerializer(response, many=True)
    return Response(serializer.data)
