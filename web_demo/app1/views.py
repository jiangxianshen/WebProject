from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from app1.forms import PersonForm
# Create your views here.
def article(request,year):
    content='the year is %s' %year
    return HttpResponse(content)

def get_name(request):
    if request.method == 'POST':
        form=PersonForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            return HttpResponse(first_name+' '+last_name)
        else:
            return HttpResponseRedirect('/error/')
    else:
        return render(request,'name.html',{'form':PersonForm()})