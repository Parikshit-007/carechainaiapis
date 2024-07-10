from django.shortcuts import render
from django.http import JsonResponse
from .models import Custom_User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from .serializers import LoginSerializer,UserSerializer,CreateUserSerializer,UpdateUserSerializer
from django.contrib.auth import get_user_model

from django.contrib.auth import login
from rest_framework import viewsets, status
from rest_framework.response import Response
from django.contrib.auth import login
from django.contrib.auth.views import LoginView as BaseLoginView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, UpdateAPIView

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
#from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
from knox import views as knox_views

class LoginView(knox_views.LoginView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data,  context={'request': request})
        if serializer.is_valid():
            user = serializer.validated_data
            login(request, user)
            response = super().post(request, format=None)   
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(response.data, status=status.HTTP_200_OK)

# @method_decorator(csrf_exempt, name='dispatch')
# class LoginView(knox_views.LoginView):
#     permission_classes = [AllowAny]

#     def post(self, request, *args, **kwargs):
#         serializer = LoginSerializer(data=request.data)
#         if serializer.is_valid():
#             user = serializer.validated_data
#             refresh = RefreshToken.for_user(user)
#             return Response({
#                 'refresh': str(refresh),
#                 'access': str(refresh.access_token),
#             }, status=status.HTTP_200_OK)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class LoginAPIView(knox_views.LoginView):
    permission_classes = (AllowAny, )
    serializer_class = LoginSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data,  context={'request': request})
        if serializer.is_valid(raise_exception=True):
            user = serializer.validated_data['user']
            login(request, user)
            response = super().post(request, format=None)
        else:
            return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

        return Response(response.data, status=status.HTTP_200_OK)

class UpdateUserAPI(UpdateAPIView):
    queryset = Custom_User.objects.all()
    serializer_class = UpdateUserSerializer
    
from knox.views import LogoutView as KnoxLogoutView

class CustomLogoutView(KnoxLogoutView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        # Knox logout implementation, which deletes the token
        super().post(request, *args, **kwargs)
        
        return Response(
            {"message": "You have successfully logged out. Thank you for using our service!"},
            status=status.HTTP_200_OK  # Use HTTP_200_OK to ensure the message is sent in the response
        )
class LogoutView(knox_views.LogoutView):
    permission_classes = [IsAuthenticated] 

    def post(self, request, *args, **kwargs):
        request._auth.delete()  
        return Response(
            {"message": "Successfully logged out"},
            status=status.HTTP_204_NO_CONTENT  
        )

@method_decorator(csrf_exempt, name='dispatch')    
class RegisterView(generics.CreateAPIView):
    #queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = CreateUserSerializer
    def post(self, request):
        serializer= CreateUserSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            user= Custom_User.objects.get(username=serializer.data['username'])
            print(user)
           # token_obj = Token.objects.get(user=user)
          
            

            
            return Response({'user': serializer.data}  , status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/api/token/',
        '/api/register/',
        '/api/token/refresh/'
    ]
    return Response(routes)

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def testEndPoint(request):
    if request.method == 'GET':
        data = f"Congratulations {request.user.username}, your API just responded to GET request"
        return Response({'response': data}, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        text = "Hello buddy"
        data = f'Congratulations, your API just responded to POST request with text: {text}'
        return Response({'response': data}, status=status.HTTP_200_OK)
    return Response({}, status.HTTP_400_BAD_REQUEST)


