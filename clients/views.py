from django.core.exceptions import ObjectDoesNotExist


from django.contrib.auth import authenticate, login, logout

from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from clients.utils import get_tokens_for_user
from houses.models import House
from .models import Client
from .serializers import RegistrationSerializer, PasswordChangeSerializer

from rest_framework.permissions import AllowAny


# Create your views here.

class RegistrationView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'success': True, 'msg': 'Register Success'}, status=status.HTTP_201_CREATED)
        return Response({'success': False, 'msg': 'User already exist!'}, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        if 'email' not in request.data or 'password' not in request.data:
            return Response({'msg': 'Credentials missing'}, status=status.HTTP_400_BAD_REQUEST)
        email = request.data['email']
        password = request.data['password']
        try:
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                auth_data = get_tokens_for_user(request.user)

                return Response({'success': True, 'msg': 'Login Success', **auth_data}, status=status.HTTP_200_OK)
        except ValueError as e:
            return Response({'success': False, 'msg': str(e)}, status=status.HTTP_401_UNAUTHORIZED)


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        logout(request)
        return Response({'success': True, 'msg': 'Successfully Logged out'}, status=status.HTTP_200_OK)


class ChangePasswordView(APIView):
    permission_classes = [IsAuthenticated, ]

    def post(self, request):
        serializer = PasswordChangeSerializer(context={'request': request}, data=request.data)
        serializer.is_valid(raise_exception=True)
        request.user.set_password(serializer.validated_data['new_password'])
        request.user.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


class GetProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            client = Client.objects.get(email=request.data['email'])
            return Response({'success': True, 'msg': client.toJson()}, status=status.HTTP_200_OK)
        except:
            return Response({'success': False, 'msg': "Forbidden"}, status=status.HTTP_403_FORBIDDEN)


class CheckLoginView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self):
        return Response({'success': True}, status=status.HTTP_200_OK)


class UpdateProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            # Primero actualizamos los campos del usuario en base a los recibidos
            # en la función
            client = Client.objects.filter(email=request.user.email)
            client.update(**request.data)
            # Si el campo email está presente, cambiamos el atributo owner de
            # las casas
            if "email" in request.data:
                client = Client.objects.get(email=request.data["email"])
                houses = House.objects.filter(owner=request.user.email)
                for h in houses:
                    h.owner = request.data["email"]
                    h.save()

            else:
                # Retornamos la información actualizada en la base de datos.
                client = Client.objects.get(email=request.user.email)
            return Response({'success': True, 'msg': client.toJson()}, status=status.HTTP_200_OK)

        except ObjectDoesNotExist:
            return Response({'success': False, 'msg': 'User does not exist in database'},
                            status=status.HTTP_404_NOT_FOUND)
