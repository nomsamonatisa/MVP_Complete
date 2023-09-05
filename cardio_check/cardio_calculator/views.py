from django.shortcuts import render, redirect
from django.http import HttpResponse

from cardio_calculator.fr import Framingham
from cardio_calculator.models import HealthData, RiskScore


def home_view(request):
    return render(request, 'registration/landing.html')


def dashboard(request):
    user = request.user.id
    health_data = HealthData.objects.filter(user_id=user).last()
    risk = RiskScore.objects.filter(user_id=user).last()

    context = {
        'health_data': health_data,
        'risk': risk
    }
    return render(request, 'cardio_calculator/dashboard.html', context)


def calculate_framingham_score(request):
    user_id = request.user.id
    if request.method == 'POST':
        # Get form data from POST request

        isMale = int(request.POST.get('gender'))
        smoker = int(request.POST.get('smoker'))
        hypertensive = int(request.POST.get('hypertensive'))
        diabetic = int(request.POST.get('diabetic'))
        age = int(request.POST.get('age'))
        blood_pressure = int(request.POST.get('systolic_blood_pressure'))
        total_cholesterol = float(request.POST.get('total_cholesterol'))
        hdl = float(request.POST.get('hdl_cholesterol'))
        if isMale == 0:
            gender = 'male'
        else:
            gender = 'female'

        HealthData.objects.create(user_id=user_id, gender=gender, age=age, is_diabetic=diabetic, is_smoker=smoker, blood_pressure=blood_pressure,
                                  total_cholesterol=total_cholesterol, hdl_cholesterol=hdl, is_hypertensive=hypertensive)
        person = Framingham(gender=isMale, age=age, diabetes=diabetic, smoker=smoker, blood_pressure=blood_pressure,
                            total_cholesterol=total_cholesterol, hdl=hdl, treated_blood_pressure=hypertensive)
        risk_score, risk_level  = person.FraminghamRisk()
        RiskScore.objects.create(user_id=user_id, risk_score=risk_score, risk_level=risk_level)
        return redirect('dashboard')
