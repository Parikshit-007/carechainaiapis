from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.urls import path, re_path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('doctor/', include('doctor.urls') ),
    path('patient/', include('patient.urls')),
    path('opd/', include('opd.urls')),
    path('accounts/', include('accounts.urls')),
    path('ipd/', include('ipd.urls')),
    path('api/staff/', include('staff.urls')),
    path('inventory/', include('inventory.urls')),
    path('emergency/', include('emergency.urls')),
   # path('analytics/', include('analytics.urls')),
    path('api/patient/', include('patient.urls')),
     path('api/ipd/', include('ipd.urls')),
    path('api/opd/', include('opd.urls')),
    path('api/hos_login', include('hos_login.urls')),
    path('api/accounts/', include('accounts.urls')),
    path('api/appointment/',include('appointment.urls')),
   #  path('api/patient_dashboard/', include('patient_dashboard.urls')),
   # patient_dashboard
    #re_path(r'^.*', TemplateView.as_view(template_name='index.html')),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)