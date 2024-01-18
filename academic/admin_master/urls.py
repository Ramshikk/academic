from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('admindepartment',views.admin_master_department,name='admindep'),
    path('admindesignation',views.admin_master_designation,name="designation"),
    path('adminqualification',views.admin_master_qualification,name="qualification"),
    path('editqualification',views.Editqualification),
    path('editingqualification',views.qualificationeditting),
    path('deleteQualification',views.deletequalification),
    path('adminemployeeCategory',views.admin_master_employee_manage,name="empcategory"),
    path('employeeedit',views.editemployee),
    path('empeditting',views.employeeEditting),
    path('deleteemployeeCat',views.deleteempcat),
    path('adminclass',views.admin_master_manage_class,name="classadding"),
    path('editclass',views.classedit),
    path('editingclass',views.classeditting),
    path('deletClass',views.classdelete),
    path('admindivision',views.admin_master_diviision_manage,name='divisionmgt'),
    path('divisionedit',views.editDivision,name='divediting'),
    path('divediting',views.divEditting),
    path('deletedivision',views.divisionDelete),
    path('editdepartment/',views. admin_department_edit,name="editdept"),
    path('editdep',views.department_editing,name="editdept"),
    path('deletedepartment/',views.department_delete,name="deletedep"),
    path('admineditdesignation/',views.admineditDesignation,name="editdesig"),
    path('editdesig/',views.designationEditting,name='editdes'),
    path('deletedesignation',views.deletedesignation,name="deldes"),
    path('Subjectmanagement',views.subjectManagement,name='subjectmgt'),
    path('subjectclassview',views.subjectclassAssignedview),
    path('sujectclassedit',views.subjectClassedit,),
    


]
