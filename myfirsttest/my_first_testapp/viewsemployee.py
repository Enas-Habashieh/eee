from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from my_first_testapp.controller.emp_controller import addemployeecontroller, deleteemployeecontroller, \
    updateemployeecontroller, getbyidemployeeycontroller, getllemployeecontroller, getemployeeparamcontroller
from my_first_testapp.dto.response.employee_response import employeeaddresponse
from my_first_testapp.serializer import EmployeeSerializer


@api_view(['POST'])
def addemployeeview(request):
    response = addemployeecontroller(request)
    respons1 =employeeaddresponse(response)
    #serializer = EmployeeSerializer(response)
    return Response(respons1)


@api_view(['delete'])
def deleteemployeeview(request, pk):
    response = deleteemployeecontroller(request, pk)
    if response is not None:
        return Response('deleted')
    else:
        return HttpResponse('not found')


@api_view(['POST'])
def updateemployeeview(request, pk):
    response = updateemployeecontroller(request, pk)
    serializer = EmployeeSerializer(response)
    return Response(serializer.data)

@api_view(['GET'])
def getbyidemployeeyview(request,pk):
    response = getbyidemployeeycontroller(request,pk)
    serializer = EmployeeSerializer(response,many=False)
    return Response(serializer.data)

@api_view(['GET'])
def getllemployeeview(request):
    response = getllemployeecontroller(request)
    serializer = EmployeeSerializer(response,many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getemployeeparamview(request):
    response = getemployeeparamcontroller(request)
    serializer = EmployeeSerializer(response,many=True)
    return Response(serializer.data)



