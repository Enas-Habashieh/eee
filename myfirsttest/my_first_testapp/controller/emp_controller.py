from my_first_testapp.service.emp_service import addemployeeservice, deleteemployeeservice, updateemployeeservice, \
    getbyidemployeeyservice, getllemployeeservice, getemployeeparamservice


def addemployeecontroller(request):
    data = request.data
    response = addemployeeservice(data)
    return response


def deleteemployeecontroller(request, pk):
    response = deleteemployeeservice(request, pk)
    return response


def updateemployeecontroller(request, pk):
    data = request.data
    response = updateemployeeservice(data, pk)
    return response


def getbyidemployeeycontroller(request, pk):
    response = getbyidemployeeyservice(request, pk)
    return response


def getllemployeecontroller(request):
    response = getllemployeeservice(request)
    return response
def getemployeeparamcontroller(request):
    response = getemployeeparamservice(request)
    return response