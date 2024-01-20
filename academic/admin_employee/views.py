from django.shortcuts import render, get_object_or_404
from django.conf  import settings
from admin_master.models import adminClass,Employee,Subject,SujectClass,Division,Department,Designation,Qualification
from admin_employee .models import EmployeeRegistration,scd,EmpSalary,SujectClass,EmployeeDesignation,Department_employee
from django.http import HttpResponse
from django.shortcuts import render
import qrcode
from django.core.files.uploadedfile import InMemoryUploadedFile
from io import BytesIO
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
import os
# Create your views here.
@csrf_exempt
def OEmployeeAdd(request):
    emparea = Employee.objects.filter(status=1)
    classlist = adminClass.objects.filter(status=1)
    divisionlist = Division.objects.filter(status=1)
    qualificationlist = Qualification.objects.filter(status=1)
    deslist = Designation.objects.filter(status=1)
    departmentlist = Department.objects.filter(status=1)
    msg = ""
    type = ""

    if request.method == 'POST':
        # Extract form data
        ename = request.POST.get("ename").strip()
        empcat = request.POST.get("empcat")
        empcatid = empcat.split("+")
        DOB= request.POST.get("dob").strip()
        mobile=request.POST.get("mobile")
        gender= request.POST.get("gender")
        email= request.POST.get("email").strip()
        qualid= request.POST.get("qualification")
        address= request.POST.get("address").strip()
        joindate= request.POST.get("joindate").strip()
        photo= request.FILES["filename"]
        desid=request.POST.get("desid")
        depid= request.POST.get("depid")
        salary= request.POST.get("salary").strip()
        date_obj = datetime.strptime(DOB, "%Y-%m-%d")

# Format the datetime object as "year-month-date"
        formatted_datedob = date_obj.strftime("%Y-%m-%d")
        date_obj1 = datetime.strptime(joindate, "%Y-%m-%d")

# Format the datetime object as "year-month-date"
        formatted_datejoindate = date_obj1.strftime("%Y-%m-%d")

        # Add more form data extraction here...

        # Validation checks
        if not ename or empcat == '0' or not mobile or not email or qualid == '0' or not address or desid == '0' or not salary:
            msg = "Please fill in all details"
            type = "warning"
        elif EmployeeRegistration.objects.filter(empname=ename, email=email).exists():
            msg = "Employee already exists"
            type = "warning"
        else:
                empcatobj = get_object_or_404(Employee, pk=int(empcatid[0]))
                desobj = get_object_or_404(Designation, pk=int(desid))
                depobj = get_object_or_404(Department, pk=int(depid))
                qualobj = get_object_or_404(Qualification, pk=int(qualid))
               
                #qr code generation
                qr_data = f"Name: {ename} \nDOB: {DOB}\nEmail:{email} \nDepartment: {depobj.depname}\nJoin Date: {joindate}"

                # Generate QR code image
                qr = qrcode.QRCode(
                    version=1,
                    error_correction=qrcode.constants.ERROR_CORRECT_L,
                    box_size=10,
                    border=4,
                )
                qr.add_data(qr_data)
                qr.make(fit=True)
                img = qr.make_image(fill_color="black", back_color="white")

                # Save the QR code image to a BytesIO object
                qr_image_io = BytesIO()
                img.save(qr_image_io, format='PNG')
                qr_image_io.seek(0)

                # Create an InMemoryUploadedFile from BytesIO
                qr_image = InMemoryUploadedFile(
                    file=qr_image_io,
                    field_name=None,
                    name=f'qr_code_{ename}_{email}.png',
                    content_type='image/png',
                    size=qr_image_io.tell(),
                    charset=None,
                )


            
              
                # Create EmployeeRegistration object
                empobj = EmployeeRegistration.objects.create(
                    empcatid=empcatobj,
                    empname=ename,
                    gender=gender,
                    dob=formatted_datedob,
                    mob=mobile,
                    email=email,
                    address=address,
                    jdate=formatted_datejoindate,
                    deptid=depobj,
                    desid=desobj,
                    qualid=qualobj,
                    salary=salary,
                    photo=photo,
                    barcode=qr_image
                )

                # Create related objects
                EmployeeDesignation.objects.create(empid=empobj, designationid=desobj, fromdate=joindate)
                EmpSalary.objects.create(empid=empobj, salary=salary, fromdate=joindate)
                Department_employee.objects.create(empid=empobj, deptid=depobj, fromdate=joindate)
                clslist=request.POST.getlist("txtclass")
                sublst=request.POST.getlist("txtsubject")
                divlst=request.POST.getlist("txtdivision")
                
                

                if clslist:
                         for clasid,subid,divsid in zip(clslist,sublst,divlst):
                            obj= scd(empid=empobj,classid=get_object_or_404(adminClass, pk=int(clasid)),
                                     divid=get_object_or_404(Division, pk=int(divsid)),
                                     subid=get_object_or_404(Subject, pk=int(subid)))
                            obj.save()
                            msg = "Teacher added successfully"
                            type = "success"

                msg = "Details added successfully"
                type = "success"

    context = {
       
        'classlist': classlist,
        'emparea': emparea,
        'divlist': divisionlist,
        'qualificationlst': qualificationlist,
        'deslist': deslist,
        'departmentlist': departmentlist,
        'message': msg,
        'type': type,
    }
    return render(request, 'employeeAdd.html', context)


def sublist(request):
    clsid= request.GET.get('id')
    subject_class_instances = SujectClass.objects.filter(classid=clsid).select_related('classid', 'sujectid')
    if subject_class_instances:
        data = [{
            'id': instance.sujectid.id,
            'subjectname': instance.sujectid.subjectname,
        } for instance in subject_class_instances]
        
        detailed_data = {
            'subjects': data,
        }
        return JsonResponse(detailed_data)
    else:
        return JsonResponse({'error': 'Subject not found for the given class'})
    
def EmployeeView(request):
     employeeList=EmployeeRegistration.objects.select_related('deptid')

     return render(request,'viewemployee.html',{'employeelist':employeeList})
def deleteEmployee(request):
    try:
        empid=request.GET['id']
        obj=EmployeeRegistration.objects.get(id=empid)
        if obj.photo:
            os.remove(obj.photo.path)
            os.remove(obj.barcode.path)
            obj.delete()
            return JsonResponse({'message': 'Data Deleted successfully'})
           
    except EmployeeRegistration.DoesNotExist:
                    return JsonResponse({'message': 'employee  not found'}, status=404)
    except Exception as e:
        return JsonResponse({'message': f'Error: {str(e)}'}, status=500)
    
def EditEmployee(request,empid):
    classlist = adminClass.objects.filter(status=1)
    divisionlist = Division.objects.filter(status=1)     
    qualificationlist = Qualification.objects.filter(status=1)
    employee_teacherdetails = scd.objects.filter(empid_id=empid).select_related('classid', 'divid', 'subid')

    employee_area=EmployeeRegistration.objects.select_related('empcatid').filter(id=empid)

    employee_details=EmployeeRegistration.objects.get(id=empid)
    if request.method == 'POST':
        # Extract form data
        ename = request.POST.get("ename").strip()
       
        DOB= request.POST.get("dob").strip()
        mobile=request.POST.get("mobile")
        gender= request.POST.get("gender")
        email= request.POST.get("email").strip()
        qualid= request.POST.get("qualification")
        address= request.POST.get("address").strip()
        joindate= request.POST.get("joindate").strip()
        if 'filename' in request.FILES:
         photo = request.FILES['filename']
    # Rest of your code for handling the file...
        else:
    # Handle the case when 'filename' is not present in request.FILES
         photo = None 
        photo= request.FILES["filename"]
        if photo == "":
             pic_path=request.POST["txtphoto"]
        else:
             pic_path= request.FILES["filename"]
             #os.remove(request.POST["txtphoto"].path)
       
        date_obj = datetime.strptime(DOB, "%Y-%m-%d")

# Format the datetime object as "year-month-date"
        formatted_datedob = date_obj.strftime("%Y-%m-%d")
        date_obj1 = datetime.strptime(joindate, "%Y-%m-%d")

# Format the datetime object as "year-month-date"
        formatted_datejoindate = date_obj1.strftime("%Y-%m-%d")

        # Add more form data extraction here...

        if not ename or not mobile or not email or qualid == '0' or not address :
            msg = "Please fill in all details"
            type = "warning"
        elif EmployeeRegistration.objects.filter(mob=mobile, email=email).exclude(id=empid).exists():
            msg = "Employee already exists"
            type = "warning"
        elif EmployeeRegistration.objects.filter( email=email).exclude(id=empid).exists():
            msg = "Email already exists"
            type = "warning"
        else:
                depid=request.POST["txtdeptid"]
                numeric_part = depid.split('(')[1].split(')')[0]
                qualobj = get_object_or_404(Qualification, pk=int(qualid))
                depobj = get_object_or_404(Department, pk=int(numeric_part))
                #qr code generation
                qr_data = f"Name: {ename} \nDOB: {DOB}\nEmail:{email} \nDepartment: {depobj.depname}\nJoin Date: {joindate}"

                # Generate QR code image
                qr = qrcode.QRCode(
                    version=1,
                    error_correction=qrcode.constants.ERROR_CORRECT_L,
                    box_size=10,
                    border=4,
                )
                qr.add_data(qr_data)
                qr.make(fit=True)
                img = qr.make_image(fill_color="black", back_color="white")

                # Save the QR code image to a BytesIO object
                qr_image_io = BytesIO()
                img.save(qr_image_io, format='PNG')
                qr_image_io.seek(0)

                # Create an InMemoryUploadedFile from BytesIO
                qr_image = InMemoryUploadedFile(
                    file=qr_image_io,
                    field_name=None,
                    name=f'qr_code_{ename}_{email}.png',
                    content_type='image/png',
                    size=qr_image_io.tell(),
                    charset=None,
                )


            # employee_area=EmployeeRegistration.objects.filter(id=empid).select_related('empcatid')
              
                # Create EmployeeRegistration object
             
                  
                employee_details.empname=ename
                employee_details.gender=gender
                employee_details.dob=formatted_datedob
                employee_details.mob=mobile
                employee_details.email=email
                employee_details.address=address
                employee_details.jdate=formatted_datejoindate
                   
                employee_details.qualid=qualobj
                   
                employee_details.photo=pic_path
                employee_details.barcode=qr_image

                employee_details.save()

                # Create related objects
              
                clslist=request.POST.getlist("txtclass")
                sublst=request.POST.getlist("txtsubject")
                divlst=request.POST.getlist("txtdivision")
                #deleting employee scd details from scd table 
                scddetails=scd.objects.filter(empid=empid)
                scddetails.delete()

                if clslist:
                        for clasid,subid,divsid in zip(clslist,sublst,divlst):
                            obj= scd(empid=employee_details,classid=get_object_or_404(adminClass, pk=int(clasid)),
                            divid=get_object_or_404(Division, pk=int(divsid)),
                            subid=get_object_or_404(Subject, pk=int(subid)))
                            obj.save()
                            msg = "Teacher updated successfully"
                            type = "success"
                
                msg = "Details updated successfully"
                type = "success"


    context={
         'classlist':classlist,
         'divisionlist':divisionlist,
         'Qualificationlist':qualificationlist,
         'employee_details':employee_details,
         'employee_teacherdetails':employee_teacherdetails,
         'employee_area':employee_area
    }
    return render(request,'editemployee.html',context)


    
     