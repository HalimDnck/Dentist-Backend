from django.shortcuts import render
from core.base.views import BaseViewSet

from patient.models import *
from patient.serializers import *


class PatientViewSet(BaseViewSet):
    queryset = Patient.objects.filter(is_deleted=False)
    serializer_class = PatientSerializer
