from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import ChaiVariety, Calculation
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
    result = None
    fn = modelForm()
    data = {'form' : fn}
    try:
        if request.method == "POST":
            form = modelForm(request.POST)
            if  form.is_valid():
                # n1 = int(request.GET['num1'])
                # n2 = int(request.GET['num2'])

                n1 = int(request.POST['num1'])
                n2 = int(request.POST['num2'])

                result = n1 + n2

                record = Calculation(num1 = n1, num2 = n2, sum=result)
                record.save()


                # return HttpResponseRedirect(("/chai/?output={}").format(result))

    except:
        result = "Kuch Bhi ?"
    
    
    all_calculations = Calculation.objects.all()
    data = {
        'form' : fn,
        'output' : result,
        'calculations': all_calculations
    }

    return render(request, 'chai/user_form.html', data)


def delete_calculation(request, calc_id):
    data = get_object_or_404(Calculation, id = calc_id)
    if request.method == 'POST':
        data.delete()
    return redirect('/chai/form')

