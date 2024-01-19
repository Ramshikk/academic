from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('employeeadd',views.OEmployeeAdd,name='employeeadd'),
    path('sublist',views.sublist),
    path('viewEmployee',views.EmployeeView),
    path('DeleteEmployee',views.deleteEmployee),
    path('Editemployee/<int:empid>',views.EditEmployee,name='Editemployee')
]

if settings.DEBUG:  
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)  
