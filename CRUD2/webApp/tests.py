from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect
from .models import company
from .forms import NewForm
# Create your views here.
def home(request):
    orglist=company.objects.all()
    return render(request,'MyApp/home.html',{'orglist':orglist})

def org_create(request):
    form=NewForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance=form.save()
        instance.save()
        return HttpResponseRedirect('/')
    context={'form':form}
    return render(request,'MyApp/create.html',context)
def org_read(request, id=None):
    instance=get_object_or_404(company,id=id)
    context={'instance':instance}
    return render(request,'MyApp/retrive.html',context)
def org_update(request,id=None):
    instance=get_object_or_404(company,id=id)
    form=NewForm(request.POST or None,request.FILES or None, instance=instance)
    if form.is_valid():
        instance=form.save()
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context={'instance':instance,'form':form}
    return render(request,'MyApp/Update.html',context)

# def org_create(request):
#     if request.method == 'POST':
#         form = NewForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('/')
#     else:
#         form = NewForm()
#     return render(request, 'MyApp/create.html',{
#         'form': form
#     })
