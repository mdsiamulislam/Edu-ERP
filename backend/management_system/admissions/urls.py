

from xml.etree.ElementInclude import include
from django.urls import path
from .views.admission_view import AdmissionListView

urlpatterns = [
    path('admissions/', AdmissionListView.as_view())
]
