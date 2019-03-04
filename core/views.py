import re
from .models import Employee
from .forms import EmployeeForm
from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required



@login_required()
def indr(request):
    templates='core/vm.html'
    ob=Employee.objects.all()
    context={
        "a":ob
    }
    return render(request,templates,context)


@login_required()
def empdetail(request,pk):
    qs=Employee.objects.get(id=pk)
    templates="core/empdetail.html"
    return render(request,templates,{"qs":qs})


@login_required()
def empdelete(request,pk):
    qs=Employee.objects.get(id=pk)
    qs.delete()
    return redirect("indr")    


@login_required()
def emp_create(request):
    b = EmployeeForm(request.POST)
    if b.is_valid():
        ab = b.save(commit=False)
        ab.save()

        return redirect('indr')
    return render(request,'core/emp_create.html',{'form':b})   
 
@login_required()
def empupdate(request,pk):
    qs=get_object_or_404(Employee ,pk=pk)
    if request.method == "POST":
        form = EmployeeForm(request.POST, instance=qs )
        if form.is_valid():
            ab = form.save(commit=False)
            ab.save()
            return redirect('indr')
    else:
        form = EmployeeForm(instance=qs)
    return render(request,'core/emp_create.html',{'form':form})    
