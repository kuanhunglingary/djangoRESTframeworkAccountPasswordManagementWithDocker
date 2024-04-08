from django.shortcuts import render
from rest_framework import generics, status, viewsets
from rest_framework.authtoken.serializers import AuthTokenSerializer

from .serializers import LoginSerializer, RegisterSerializer

# Create your views here.


class RegisterViewSet(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)

        if serializer.is_valid():
            serializer.save()

            response = {"message": "success", "data": serializer.data}

            return response(data=response, status=status.HTTP_200_OK)


class LoginViewSet(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        response = {"message": "success", "data": serializer.data}
        return response(serializer.data, status=status.HTTP_200_OK)
