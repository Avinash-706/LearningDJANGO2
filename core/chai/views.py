from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ChaiVariety
from .forms import modelForm
from django.shortcuts import get_object_or_404

# Create your views here.
def all_chai(request):
    if(request.method == "GET"):
        output = request.GET.get('output')
    chais = ChaiVariety.objects.all()
    return render(request, 'chai/all_chai.html', {'chais' : chais, 'output':output}) 


def chai_detail(request, chai_id):
    chai = get_object_or_404(ChaiVariety, pk = chai_id)
    return render(request, 'chai/chai_detail.html', {'chai' : chai})


#form
def userForm(request):
    sum = None
    fn = modelForm()
    data = {'form' : fn}
    try:
        if request.method == "POST":
            # n1 = int(request.GET['num1'])
            # n2 = int(request.GET['num2'])

            n1 = int(request.POST['num1'])
            n2 = int(request.POST['num2'])


            sum = n1 + n2
            data = {
                'form' : fn,
                'output' : sum
            }
            # return HttpResponseRedirect(("/chai/?output={}").format(sum))

    except:
        sum = "Kuch Bhi ?"
    return render(request, 'chai/user_form.html', data)