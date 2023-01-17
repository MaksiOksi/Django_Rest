from django.shortcuts import render
from rest_framework import generics
from .serializers import CarDetailSerializer, CarsListSerializer
from cars.models import Car
from .permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAdminUser
from rest_framework.authentication import TokenAuthentication


class CarCreateView(generics.CreateAPIView):
    serializer_class = CarDetailSerializer


class CarsListView(generics.ListAPIView):
    serializer_class = CarsListSerializer
    queryset = Car.objects.all()
    permission_classes = (IsAdminUser, )


class CarDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CarDetailSerializer
    authentication_classes = (TokenAuthentication, )
    queryset = Car.objects.all()
    permission_classes = (IsOwnerOrReadOnly, )
