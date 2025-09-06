from django.shortcuts import render
from django.http import HttpResponse
from .models import ChaiVariety
from django.shortcuts import get_object_or_404

# Create your views here.
def all_chai(request):
    chais = ChaiVariety.objects.all()
    return render(request, 'chai/all_chai.html', {'chais' : chais}) 


def chai_detail(request, chai_id):
    chai = get_object_or_404(ChaiVariety, pk = chai_id)
    return render(request, 'chai/chai_detail.html', {'chai' : chai})


#form
def userFormGET(request):
    sum = 0
    try:
        n1 = int(request.GET['num1'])
        n2 = int(request.GET['num2'])
        sum = n1 + n2
    except:
        sum = "Kuch Bhi ?"
    return render(request, 'chai/user_form.html', {"total":sum})