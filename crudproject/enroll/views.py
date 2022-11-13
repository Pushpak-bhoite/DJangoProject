from django.shortcuts import render
from enroll.forms import StudentRegistration
# Create your views here.

def add_show(request):
    if request.method == "POST":
        fm = StudentRegistration(request.post)
    else:
        fm = StudentRegistration()
    
    return render(request , 'enroll/addandshow.html',{'form':fm})

    

