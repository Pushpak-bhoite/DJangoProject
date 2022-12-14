from django.shortcuts import render ,HttpResponseRedirect 
from enroll.forms import StudentRegistration
from enroll.models import User
# Create your views here.

# This Function will Add new Item and Show All Items
def add_show(request):
    if request.method == "POST":
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['emp_name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['work']
            reg = User(emp_name=nm , email=em , work=pw )
            reg.save()
            fm = StudentRegistration()#this sentese shows blank data form
    else:
        fm = StudentRegistration()

    
    stud = User.objects.all()
    return render(request , 'enroll/addandshow.html',{'form':fm ,'stu':stud})
    
    # This Function will Update
def update_data(request , id ):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(request.POST ,instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(request.POST ,instance = pi)
    return render(request , 'enroll/updatestudent.html' , {'form':fm})



    # This Function Will Delete 
def delete_data(request , id ):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')
    
