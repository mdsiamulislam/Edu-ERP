
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('institute/', include('institute.urls')),
    path('admissions/', include('admissions.urls')),
    path('fees/', include('fees.urls')),
    path('api/', include('api.urls')),
]
