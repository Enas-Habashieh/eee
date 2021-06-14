from my_first_testapp.models import Department


def adddepartmentservice(request):
    department = Department()
    department.name = request.get('name')
    department.save()
    return department


def deletedepartmentService(request, pk):
    try:
        data = Department.objects.get(id=pk)
        if data is not None:
            data.delete()
            return "delete"

    except:
        return None

def updatedepartmentservice(request,pk):
   department = Department.objects.get(id=pk)
   department.name = request.get('name')
   department.save()
   return department

def getbyiddepartmentservice(request,pk):
    department = Department.objects.get(id=pk)
    return department

def getalldepartmentservice(request):
    department = Department.objects.all()
    return department
