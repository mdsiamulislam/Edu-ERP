
from django.urls import path
from .views import InstituteInfoView
from .view.academic_config_views import AcademicConfigView

urlpatterns = [
    # Define your institute app URLs here
    path('', InstituteInfoView.as_view(), name='institute-list'),
    path('academic-config/', AcademicConfigView.as_view(), name='academic-config-list'),
]
