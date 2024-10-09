from django.shortcuts import render,redirect
from django.http import HttpResponse
from myapp.models import *
from myapp.form import *
def usershow(req):
    form=customform()
    if req.method=='POST':
        un=req.POST.get('username')
        fn=req.POST.get('first_name')
        ln=req.POST.get('last_name')
        em=req.POST.get('email')
        pw=req.POST.get('password')
        customModel.objects.create(username=un,first_name=fn,last_name=ln,email=em,password=pw)
    return render(req, 'home.html',{'form':form})

def userview(req):
    form=customModel.objects.all()
    return render(req, 'view.html',{'form':form})

def update(req,id):
    obj=customModel.objects.get(id=id)
    form=customform(initial={'username':obj.username,'first_name':obj.first_name,'last_name':obj.last_name,
                             'email':obj.email,'password':obj.password})
    if req.method=='POST':
        un=req.POST.get('username')
        fn=req.POST.get('first_name')
        ln=req.POST.get('last_name')
        em=req.POST.get('email')
        pw=req.POST.get('password')
        obj=customModel(id=id,username=un,first_name=fn,last_name=ln,email=em,password=pw)
        obj.save()
        return redirect('userview')
    return render(req, 'home.html',{'form':form})

def delete(req,id):
    obj=customModel.objects.get(id=id).delete()
    return redirect('userview')