from django.shortcuts import render,get_object_or_404, redirect
from .models import Machine
from django.conf import settings
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    machines = Machine.objects.order_by('-machine_date')

    context = {
        'machines' : machines
    }
    return render(request, 'machines/machines.html', context)

@login_required(login_url="/accounts/login/")
def machine(request, machine_id):
    machine = get_object_or_404(Machine, pk=machine_id)
    context = {
        'machine' : machine
    }
    return render(request, 'machines/machine.html', context)