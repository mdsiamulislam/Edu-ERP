
from django.urls import path
from .views import InstituteInfoView

urlpatterns = [
    # Define your institute app URLs here
    path('', InstituteInfoView.as_view(), name='institute-list'),
]
