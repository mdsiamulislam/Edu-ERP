
from django.urls import path

from .views import InstituteInfoView
from .view.academic_config_views import AcademicConfigView
from .view.class_views import ClassView

urlpatterns = [
    # Define your institute app URLs here
    path('', InstituteInfoView.as_view(), name='institute-list'),
    path('academic-config/', AcademicConfigView.as_view(), name='academic-config-list'),
    path('class/', ClassView.as_view(), name='class-list'),
]
