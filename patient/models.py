from django.db import models
from core.base.models import BaseModel


class Patient(BaseModel):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    id_number = models.CharField(max_length=11)
    gender = models.ForeignKey("system.Gender", on_delete=models.SET_NULL, null=True)

    phone_number = models.CharField(max_length=15)
    email = models.CharField(max_length=64, null=True)
    address = models.TextField(max_length=256, null=True)
    date_of_birth = models.DateField(null=True)

    referral_source = models.ForeignKey(
        "system.ReferralSource", on_delete=models.SET_NULL, null=True
    )

    allergies = models.ManyToManyField(
        "system.Allergy", through="PatientAllergy", blank=True
    )


class PatientInsurance(BaseModel):
    patient = models.ForeignKey(
        "patient.Patient", on_delete=models.CASCADE, related_name="insurance"
    )

    insurance_provider = models.ForeignKey(
        "system.InsuranceProvider", on_delete=models.SET_NULL, null=True
    )
    insurance_policy_number = models.CharField(max_length=16, blank=True, null=True)
    insurance_validation_date = models.DateField(blank=True, null=True)


class PatientAllergy(BaseModel):
    patient = models.ForeignKey("patient.Patient", on_delete=models.CASCADE)
    allergy = models.ForeignKey("system.Allergy", on_delete=models.CASCADE)

    description = models.CharField(max_length=600, null=True, blank=True)
