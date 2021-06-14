import list1 as list1

from my_first_testapp.models import Employee


def addemployeeservice(request):
    employee = Employee()
    employee.full_name = request.get('full_name')
    employee.department_id = request.get('department')
    employee.mobile = request.get('mobile')
    employee.salary = request.get('salary')
    employee.save()
    return employee


def deleteemployeeservice(request, pk):
    try:
        data = Employee.objects.get(id=pk)
        if data is not None:
            data.delete()
            return "delete"

    except:
        return None


def updateemployeeservice(request, pk):
    employee = Employee.objects.get(id=pk)
    employee.full_name = request.get('full_name')
    employee.department_id = request.get('department_id')
    employee.mobile = request.get('mobile')
    employee.salary = request.get('salary')
    employee.save()
    return employee


def getbyidemployeeyservice(request, pk):
    employee = Employee.objects.get(id=pk)
    return employee


def getllemployeeservice(request):
    employee = Employee.objects.all()
    return employee


def getemployeeparamservice(request):
    var = request.GET.get('department_id')
    data = Employee.objects.filter(department_id=var)
    list1 = []
    for i in data:
        list1.append(i)
    return list1
