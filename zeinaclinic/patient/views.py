from django.shortcuts import get_object_or_404, render, redirect
from .models import Patient
from .forms import PatientForm
from django.db.models import Q

from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render
from .models import Patient

def home(request):
    query = request.GET.get('q', '')

    # 1. Filter the list
    patients_list = Patient.objects.filter(
        Q(nome__icontains=query) |
        Q(cognome__icontains=query) |
        Q(numero_cartella__icontains=query) |
        Q(nazionalita__icontains=query)
    ).order_by('cognome')

    # 2. Apply pagination AFTER filtering
    paginator = Paginator(patients_list, 10)  # 10 per page
    page_number = request.GET.get('page')
    patients = paginator.get_page(page_number)

    # 3. Send both patients & query to template
    return render(request, 'patient/home.html', {
        'patients': patients,
        'query': query
    })


from django.shortcuts import get_object_or_404

def delete_patient(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    if request.method == 'POST':
        patient.delete()
        return redirect('home')
    return render(request, 'patient/confirm_delete.html', {'patient': patient})

def add_patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PatientForm()
    return render(request, 'patient/add_patient.html', {'form': form})

def edit_patient(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    if request.method == 'POST':
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PatientForm(instance=patient)
    return render(request, 'patient/edit_patient.html', {'form': form, 'patient': patient})
