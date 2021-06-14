from rest_framework.response import Response

from my_first_testapp.service.dep_service import adddepartmentservice, deletedepartmentService, updatedepartmentservice, \
    getbyiddepartmentservice, getalldepartmentservice


def adddepartmentcontroller(request):
    data = request.data
    response = adddepartmentservice(data)
    return response


def deletedepartmentController(request, pk):
    response = deletedepartmentService(request, pk)
    return response
def updatedepartmentController(request,pk):
    data = request.data
    response = updatedepartmentservice(data,pk)
    return response
def getbyiddepartmentcontroller(request, pk):
    response = getbyiddepartmentservice(request,pk)
    return response
def getalldepartmentcontroller(request):
    response = getalldepartmentservice(request)
    return response