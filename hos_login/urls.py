from django.urls import path
from .views import HospitalListCreateAPIView, HospitalRetrieveUpdateDestroyAPIView, UserListCreateAPIView, UserLoginAPIView, UserRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('hospitals/', HospitalListCreateAPIView.as_view(), name='hospital-list-create'),
    path('hospitals/<int:pk>/', HospitalRetrieveUpdateDestroyAPIView.as_view(), name='hospital-detail'),
    path('users/', UserListCreateAPIView.as_view(), name='user-list-create'),
    path('users/<int:pk>/', UserRetrieveUpdateDestroyAPIView.as_view(), name='user-detail'),
    path('login/', UserLoginAPIView.as_view(), name='user-login'),
]
