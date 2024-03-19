# from django.urls import path
# #from .views import HospitalListCreateAPIView, HospitalRetrieveUpdateDestroyAPIView, UserListCreateAPIView, UserLoginAPIView, UserRetrieveUpdateDestroyAPIView
# from .views import UserSignupView, UserLoginView
# urlpatterns = [
#     # path('hospitals/', HospitalListCreateAPIView.as_view(), name='hospital-list-create'),
#     # path('hospitals/<int:pk>/', HospitalRetrieveUpdateDestroyAPIView.as_view(), name='hospital-detail'),
#     # path('users/', UserListCreateAPIView.as_view(), name='user-list-create'),
#     # path('users/<int:pk>/', UserRetrieveUpdateDestroyAPIView.as_view(), name='user-detail'),
#     # path('login/', UserLoginAPIView.as_view(), name='user-login'),

#         path('signup/', UserSignupView.as_view(), name='signup'),
#     path('login/', UserLoginView.as_view(), name='login'),

# ]

from . import views
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', views.RegisterView.as_view(), name='auth_register'),
    path('test/', views.testEndPoint, name='test'),
    path('', views.getRoutes),
]