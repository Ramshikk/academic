from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from admin_master.models import Department,Designation,Division,adminClass,Qualification,Employee,Subject,SujectClass
from django.http import HttpResponse,JsonResponse
from django.conf import settings


# Create your views here.
@csrf_exempt
def admin_master_department(request):
    deplist=Department.objects.all().values
    msg=""
    if request.POST:
       
        type=""
        deppname=request.POST["depname"].strip()
        deppcode=request.POST["depcode"].strip()
        if deppname == '' and deppcode == '':
            msg="Please fill details"
            type='error'
            return render(request,'admin_master_department.html',{'message':msg,'type':type,'deplist':deplist})

        elif Department.objects.filter(depname=deppname).exists() or Department.objects.filter(depcode=deppcode).exists():
            msg="Department name  and code already exist"
            type="warning"
            return render(request,'admin_master_department.html',{'message':msg,'type':type,'deplist':deplist})
        else:
            depadd=Department(depname=deppname,depcode=deppcode)
            depadd.save()
            msg="Department added successfully"
            type="success"
            return render(request,'admin_master_department.html',{'message':msg,'type':type,'deplist':deplist})

        
    return render(request,'admin_master_department.html',{'deplist':deplist,'message':msg})



def admin_department_edit(request):
    depid=request.GET['id']
    result=Department.objects.get(id=depid)
    detailed_data = {
        'deptname':result.depname,
        'deptcode':result.depcode,
        'status':result.status,

    }
    return JsonResponse(detailed_data)



def department_editing(request):
    if request.GET:
        depid=int(request.GET['id'])
   
        depname = request.GET['depname']
        depcode = request.GET['depcode']
        status = request.GET['status']
        msg=""

        if not depname or not depcode:
          return JsonResponse({'message': 'please fill details'})
        elif Department.objects.filter(depname=depname).exclude(id=depid).exists() or Department.objects.filter(depcode=depcode).exclude(id=depid).exists()  :
             return JsonResponse({'message': 'departmet name  or code exist already'})
        
        else:
                try:
                    details = Department.objects.get(id=depid)
                    details.depname = depname
                    details.depcode = depcode
                    details.status = status
                    details.save()

                    return JsonResponse({'message': 'Data updated successfully'})
           
                except Department.DoesNotExist:
                    return JsonResponse({'message': 'Department not found'}, status=404)
        
    else:
        return JsonResponse({'message': 'Department not added'})
   

def department_delete(request):
    try:
        depid=int(request.GET['id'])
        result=Department.objects.get(id=depid,status=0)
        result.delete() 
        return JsonResponse({'message': 'Data Deleted successfully'})
           
    except Department.DoesNotExist:
                    return JsonResponse({'message': 'Department not found'}, status=404)
    except Exception as e:
        return JsonResponse({'message': f'Error: {str(e)}'}, status=500)

    #return  redirect('admindep')
    

@csrf_exempt
def admin_master_designation(request):
    msg=""
    deslist=Designation.objects.all().values
    if request.POST:
        
        desiname=request.POST["designame"].strip()
        desicode=request.POST["descode"].strip()
        if desiname == '' and desicode == '':
            msg="Please fill details"
            type='error'
            return render(request,'admin_master_designation.html',{'message':msg,'type':type,'deslist':deslist})

        elif Designation.objects.filter(desname=desiname).exists() or Designation.objects.filter(descode=desicode).exists():
            msg="Designation name  and code already exist"
            type="warning"
            return render(request,'admin_master_designation.html',{'message':msg,'type':type,'deslist':deslist})
        else:
            desadd=Designation(desname=desiname,descode=desicode)
            desadd.save()
            msg="Designation added successfully"
            type="success"
            return render(request,'admin_master_designation.html',{'message':msg,'type':type,'deslist':deslist})

        
    return render(request,'admin_master_designation.html',{'message':msg,'deslist':deslist})   
         
   #get the designation details on the popup
def admineditDesignation(request):
    desid=request.GET['id']
    result=Designation.objects.get(id=desid)
    detailed_data = {
        'desname':result.desname,
        'descode':result.descode,
        'status':result.status,

    }
    return JsonResponse(detailed_data)
    
def designationEditting(request):
    if request.GET:
        depid=int(request.GET['id'])
   
        desname = request.GET['desname']
        descode = request.GET['descode']
        status = request.GET['status']
        msg=""

        if not desname or not descode:
          return JsonResponse({'message': 'please fill details'})
        elif Designation.objects.filter(desname=desname).exclude(id=depid).exists() or Designation.objects.filter(descode=descode).exclude(id=depid).exists()  :
             return JsonResponse({'message': 'designation name  or code exist already'})
        
        else:
                try:
                    details = Designation.objects.get(id=depid)
                    details.desname = desname
                    details.descode = descode
                    details.status = status
                    details.save()

                    return JsonResponse({'message': 'Data updated successfully'})
           
                except Designation.DoesNotExist:
                    return JsonResponse({'message': 'Designation not found'}, status=404)
        
    else:
        return JsonResponse({'message': 'Designation not added'})
   
def deletedesignation(request):
     
    try:
        desid=int(request.GET['id'])
        result=Designation.objects.get(id=desid,status=0)
        result.delete() 
        return JsonResponse({'message': 'Data Deleted successfully'})
           
    except Department.DoesNotExist:
                    return JsonResponse({'message': 'Designation not found'}, status=404)
    except Exception as e:
        return JsonResponse({'message': f'Error: {str(e)}'}, status=500)
    
@csrf_exempt
def admin_master_qualification(request):
    msg=""
    type=""
    qualist=Qualification.objects.all().values
    if request.POST:
        
        qualname=request.POST["qualname"].strip()
        if qualname == '':
            msg="Please fill details"
            type='error'
        elif Qualification.objects.filter(qualname=qualname).exists() :
            msg="qualification name  already exist"
            type="warning"
         
        else:
            qualadd=Qualification(qualname=qualname)
            qualadd.save()
            msg="qualification  added successfully"
            type="success"
           
    context={
         'message':msg,'type':type,'qualist':qualist}
                 
    return render(request,'admin_master_qualification.html',context)  

def Editqualification(request):
    desid=request.GET['id']
    result=Qualification.objects.get(id=desid)
    detailed_data = {
        'qualname':result.qualname,
        'status':result.status,

    }
    return JsonResponse(detailed_data)
def qualificationeditting(request):
    if request.GET:
        depid=int(request.GET['id'])
   
        qualname = request.GET['qualname']
        status = request.GET['status']
        msg=""

        if not qualname :
          return JsonResponse({'message': 'please fill details'})
        elif Qualification.objects.filter(qualname=qualname).exclude(id=depid).exists()  :
            return JsonResponse({'message': 'qualification name   exist already'})
        
        else:
                try:
                    details = Qualification.objects.get(id=depid)
                    details.qualname = qualname
                    details.status = status
                    details.save()

                    return JsonResponse({'message': 'Data updated successfully'})
           
                except Qualification.DoesNotExist:
                    return JsonResponse({'message': 'qualification not found'}, status=404)
        
    else:
        return JsonResponse({'message': 'qualification not added'})
    
def  deletequalification(request):
     
    try:
        qualid=int(request.GET['id'])
        result=Qualification.objects.get(id=qualid,status=0)
        result.delete() 
        return JsonResponse({'message': 'Data Deleted successfully'})
           
    except Qualification.DoesNotExist:
                    return JsonResponse({'message': 'qualification not found'}, status=404)
    except Exception as e:
        return JsonResponse({'message': f'Error: {str(e)}'}, status=500)
    
#employee details
@csrf_exempt
def admin_master_employee_manage(request):
    msg=""
    type=""
    emplist=Employee.objects.all()
    if request.method == 'POST':
        
        empname=request.POST["empname"].strip()
        area=request.POST["area"].strip()
        if empname == '' :
            msg="Please fill details"
            type='error'
        elif Employee.objects.filter(empname=empname).exists():
            msg="employee name   already exist"
            type="warning"
        elif Employee.objects.exclude(emparea=5).filter(emparea=area).exists():
            msg="employee area   already exist"
            type="warning"
        else:
            empadd=Employee(empname=empname,emparea=area)
            empadd.save()
            msg="Employee added successfully"
            type="success"
    context={
            'settings':settings,
            'message':msg,
            'type':type,
            'emplist':emplist
        }
        
    return render(request,'admin_master_employee_manage.html',context)   
   
def editemployee(request):
     
    empid=request.GET['id']
    result=Employee.objects.get(id=empid)
    detailed_data = {
        'empname':result.empname,
        'emparea':result.emparea,
        'status':result.status,

    }
    return JsonResponse(detailed_data)
def employeeEditting(request):
    if request.GET:
        empid=int(request.GET['id'])
   
        empname = request.GET['empname']
        emparea = request.GET['emparea']
        status = request.GET['status']
        msg=""

        if not empname :
          return JsonResponse({'message': 'please fill details'})
        elif Employee.objects.filter(empname=empname).exclude(id=empid).exists()  :
            return JsonResponse({'message': 'employee category name   exist already'})
       
        else:
                try:
                    details = Employee.objects.get(id=empid)
                    details.empname = empname
                    details.emparea = emparea
                    details.status = status
                    details.save()

                    return JsonResponse({'message': 'Data updated successfully'})
           
                except Employee.DoesNotExist:
                    return JsonResponse({'message': 'Employee not found'}, status=404)
        
    else:
            return JsonResponse({'message': 'employee not added'})

# admin class details
@csrf_exempt
def admin_master_manage_class(request):
    msg=""
    clslist=adminClass.objects.all().values
    if request.POST:
        
        clsname=request.POST["clsname"].strip()
        
        if clsname == '':
            msg="Please fill details"
            type='error'
            return render(request,'admin_master_manage_class.html',{'message':msg,'type':type,'clslist':clslist})

        elif adminClass.objects.filter(clsname=clsname).exists() :
            msg="class name  already exist"
            type="warning"
            return render(request,'admin_master_manage_class.html',{'message':msg,'type':type,'clslist':clslist})
        else:
            clsadd=adminClass(clsname=clsname)
            clsadd.save()
            msg="Class  added successfully"
            type="success"
            return render(request,'admin_master_manage_class.html',{'message':msg,'type':type,'clslist':clslist})

        
    return render(request,'admin_master_manage_class.html',{'message':msg,'clslist':clslist})   

def classedit(request):
     
    clsid=request.GET['id']
    result=adminClass.objects.get(id=clsid)
    detailed_data = {
        'clsname':result.clsname,
        'status':result.status,

    }
    return JsonResponse(detailed_data)

def classeditting(request):
    if request.GET:
        depid=int(request.GET['id'])
   
        clsname = request.GET['clsname']
        status = request.GET['status']
        msg=""

        if not clsname :
          return JsonResponse({'message': 'please fill details'})
        elif adminClass.objects.filter(clsname=clsname).exclude(id=depid).exists()  :
            return JsonResponse({'message': 'class name   exist already'})
        
        else:
                try:
                    details = adminClass.objects.get(id=depid)
                    details.clsname = clsname
                    details.status = status
                    details.save()

                    return JsonResponse({'message': 'Data updated successfully'})
           
                except Designation.DoesNotExist:
                    return JsonResponse({'message': 'class not found'}, status=404)
        
    else:
        return JsonResponse({'message': 'class not added'})
    
def classdelete(request):
    try:
        clsid=int(request.GET['id'])
        result=adminClass.objects.get(id=clsid,status=0)
        result.delete() 
        return JsonResponse({'message': 'Data Deleted successfully'})
           
    except adminClass.DoesNotExist:
            return JsonResponse({'message': 'class not found'}, status=404)
    except Exception as e:
            return JsonResponse({'message': f'Error: {str(e)}'}, status=500)

    #admin division
@csrf_exempt
def admin_master_diviision_manage(request):
    msg=""
    divlist=Division.objects.all().values
    if request.POST:
        
        divname=request.POST["txtdivision"].strip()
        
        if divname == '':
            msg="Please fill details"
            type='error'
            return render(request,'admin_master_diviision_manage.html',{'message':msg,'type':type,'divlist':divlist})

        elif Division.objects.filter(divname=divname).exists() :
            msg="Division name  already exist"
            type="warning"
            return render(request,'admin_master_diviision_manage.html',{'message':msg,'type':type,'divlist':divlist})
        else:
            divadd=Division(divname=divname)
            divadd.save()
            msg="Division  added successfully"
            type="success"
            return render(request,'admin_master_diviision_manage.html',{'message':msg,'type':type,'divlist':divlist})

        
    return render(request,'admin_master_diviision_manage.html',{'message':msg,'divlist':divlist})   

def editDivision(request):
    desid=request.GET['id']
    result=Division.objects.get(id=desid)
    detailed_data = {
        'divname':result.divname,
        'status':result.status,

    }
    return JsonResponse(detailed_data)


def divEditting(request):
    if request.GET:
        depid=int(request.GET['id'])
   
        divname = request.GET['divname']
        status = request.GET['status']
        msg=""

        if not divname :
          return JsonResponse({'message': 'please fill details'})
        elif Division.objects.filter(divname=divname).exclude(id=depid).exists()  :
            return JsonResponse({'message': 'division name   exist already'})
        
        else:
                try:
                    details = Division.objects.get(id=depid)
                    details.divname = divname
                    details.status = status
                    details.save()

                    return JsonResponse({'message': 'Data updated successfully'})
           
                except Designation.DoesNotExist:
                    return JsonResponse({'message': 'Division not found'}, status=404)
        
    else:
        return JsonResponse({'message': 'Division not added'})
    

def divisionDelete(request):
     
    try:
        divid=int(request.GET['id'])
        result=Division.objects.get(id=divid,status=0)
        result.delete() 
        return JsonResponse({'message': 'Data Deleted successfully'})
           
    except Division.DoesNotExist:
                    return JsonResponse({'message': 'Division not found'}, status=404)
    except Exception as e:
        return JsonResponse({'message': f'Error: {str(e)}'}, status=500)
def deleteempcat(request):
    try:
        empid=int(request.GET['id'])
        result=Employee.objects.get(id=empid,status=0)
        result.delete() 
        return JsonResponse({'message': 'Data Deleted successfully'})
           
    except Employee.DoesNotExist:
                    return JsonResponse({'message': 'employee category not found'}, status=404)
    except Exception as e:
        return JsonResponse({'message': f'Error: {str(e)}'}, status=500)
    

from django.shortcuts import render, get_object_or_404
from django.db import IntegrityError, transaction
from .models import Subject, SujectClass, adminClass

def subjectManagement(request):
    subjectlist=Subject.objects.filter(status=1)
    clslist = adminClass.objects.filter(status=1)
    msg = ""
    type = ""

    if request.method == 'POST':
        subname = request.POST.get("subname", "").strip()

        if not subname:
            msg = "Please fill subject"
            type = "warning" 
        elif Subject.objects.filter(subjectname=subname).exists():
            msg = "Subject name already exists"
            type = "warning" 
        else:
            try:
                with transaction.atomic():
                    subobj, created = Subject.objects.get_or_create(subjectname=subname)

                    checked_items = request.POST.getlist('chkchild')

                    if checked_items:
                        for class_id in checked_items:
                            admin_class = get_object_or_404(adminClass, pk=int(class_id))
                            subclass = SujectClass(sujectid=subobj, classid=admin_class)
                            subclass.save()

                        msg = "Details added successfully"
                        type = "success" 
                    else:
                        msg = "Please select at least one class"
                        type = "warning" 

            except IntegrityError:
                msg = "An error occurred. Please try again."
                type = "danger"  

    context = {
        'message': msg,
        'type': type,
        'clslist': clslist,
        'subjectlist':subjectlist
    }      
     
    return render(request, 'admin_master_subjectManagement.html', context)


def subjectclassAssignedview(request):
    subid = request.GET.get('id')
    try:
        subject_class_instances = SujectClass.objects.filter(sujectid__id=subid).select_related('classid', 'sujectid')
        if subject_class_instances:
            class_names = [instance.classid.clsname for instance in subject_class_instances]
            if subject_class_instances.first().sujectid.status == 1:
                 status='Active'
            else:
                 status='Deactive'
            detailed_data = {
                'subjectname': subject_class_instances.first().sujectid.subjectname,
                 'status': status,
                'classnames': class_names,
            }
            return JsonResponse(detailed_data)
        else:
            return JsonResponse({'error': 'class and subject not found for the given id'})
    except Exception as e:
        return JsonResponse({'error': str(e)})
    
def subjectClassedit(request):
    subid = request.GET.get('id')
    try:
        subject_class_instances = SujectClass.objects.filter(sujectid__id=subid).select_related('classid', 'sujectid')
        if subject_class_instances:
            class_names = [instance.classid.clsname for instance in subject_class_instances]
            detailed_data = {
                'subjectname': subject_class_instances.first().sujectid.subjectname,
                'status': subject_class_instances.first().sujectid.status,
                'classnames': class_names,
            }
            return JsonResponse(detailed_data)
        else:
            return JsonResponse({'error': 'class and subject not found for the given id'})
    except Exception as e:
        return JsonResponse({'error': str(e)})

    

