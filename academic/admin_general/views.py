from django.shortcuts import render

# Create your views here.
def adminsettings(request):
    return render(request,'admin_setting.html')