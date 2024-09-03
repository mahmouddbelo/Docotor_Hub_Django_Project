from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Specialization, Area, Doctor


def home(request):
    specializations = Specialization.objects.all()
    areas = Area.objects.all()
    return render(request, 'main/home.html', {'specializations': specializations, 'areas': areas})

@login_required
def search_results(request):
    specialization = request.GET.get('specialization')
    area = request.GET.get('area')
    doctors = Doctor.objects.filter(specialization__name=specialization, area__name=area)
    return render(request, 'main/search_results.html', {'doctors': doctors})

@login_required
def doctor_details(request, doctor_id):
    doctor = Doctor.objects.get(id=doctor_id)
    return render(request, 'main/doctor_details.html', {'doctor': doctor})