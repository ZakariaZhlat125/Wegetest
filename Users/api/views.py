from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets ,status
from rest_framework.decorators import api_view ,permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework_jwt.settings import api_settings
from ..models import User,Profile
from .serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializer


@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user= serializer.save()
        profile = Profile.objects.create(user=user ,name=user.email)
        return Response(serializer.data , status=status.HTTP_201_CREATED)
    return Response(serializer.errors ,status = status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([AllowAny])
def user_login(request):
    email = request.data.get('email')
    password = request.data.get('password')

    if email and password:
        user = authenticate(request, email=email, password=password)

        if user:
            login(request, user)

         
            jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
            jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
            payload = jwt_payload_handler(user)
            token = jwt_encode_handler(payload)

          
            return Response({
                'token': token,
                'name': user.profile.name, 
                'email': user.email,
            }, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    else:
        return Response({'message': 'Both email and password are required'}, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['POST'])
# @login_required
# def user_logout(request):
#     logout(request)
#     return Response({'message': 'Logout successful'}, status=status.HTTP_200_OK)