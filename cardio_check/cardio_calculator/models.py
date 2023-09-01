from django.db import models

from system_management.models import CustomUser

# Create your models here.
class HealthData(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    age = models.IntegerField(max_length=2)
    gender = models.CharField(max_length=6)
    blood_pressure = models.IntegerField(max_length=3)
    hdl_cholesterol = models.IntegerField(max_length=5)
    total_cholesterol = models.IntegerField(max_length=5)
    is_diabetic = models.BooleanField()
    is_smoker = models.BooleanField()
    is_hypertensive = models.BooleanField()
    date = models.DateTimeField(auto_now_add=True)


class RiskScore(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    risk_score =  models.IntegerField(max_length=3)
    date = models.DateTimeField(auto_now_add=True)