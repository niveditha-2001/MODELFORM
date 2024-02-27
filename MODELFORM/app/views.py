from django.shortcuts import render,HttpResponse

# Create your views here.
from app.forms import empform
from app.models import emp


def insert(request):
    if request.method=='GET':
        var=empform()
        return render(request,'sam.html',{'var':var})
    elif request.method=='POST':
        v=empform(request.POST)
        if v.is_valid():
            v.save()
            return HttpResponse('data stored in a table')
def read(request):
    var=emp.objects.all()
    return render(request,'read.html',{'var':var})


def update(request,pk):
    a=emp.objects.get(id=pk)
    if request.method=='GET':
        var=empform(instance=a)
        return render(request,'sam.html',{'var':var})
    elif request.method=='POST':
        v=empform(request.POST,instance=a)
        if v.is_valid():
            v.save()
            return HttpResponse('data updated in a table')

def delete(request,pk):
    emp.objects.filter(id=pk).delete()
    return HttpResponse('data deleted from the table')
