from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from doctor.views.views import DoctorListCreateView, DoctorRetrieveUpdateDestroyView
urlpatterns = [
  path('api/doctors/', DoctorListCreateView.as_view(), name='doctor-list-create'),
  path('api/doctors/<int:pk>/', DoctorRetrieveUpdateDestroyView.as_view(), name='doctor-retrieve-update-destroy'),
  path('doctors/', DoctorListCreateView.as_view(), name='doctor-list-create'),
  path('doctors/<int:pk>/', DoctorRetrieveUpdateDestroyView.as_view(), name='doctor-retrieve-update-destroy'),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)