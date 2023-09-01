from django.urls import path
from cardio_calculator import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('calculate_risk/', views.calculate_framingham_score,
         name='calculate_framingham_score'),
]
