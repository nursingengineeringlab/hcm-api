from django.shortcuts import render
from django.contrib.auth.models import User, Group
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.parsers import JSONParser
from data_api.serializers import UserSerializer, GroupSerializer
from data_api.models import Senior
from data_api.utils import get_model_by_name, url_params_validation
import json
from rest_framework.decorators import api_view

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class SeniorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Senior.objects.all()
    serializer_class = Senior.get_serializer()
    permission_classes = [permissions.IsAuthenticated]
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        user = instance.user
        user.delete()
        return super(SeniorViewSet, self).destroy(request, *args, **kwargs)



class SensorDataViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
	"""
    filterset_fields = ['senior',]
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def get_queryset(self):
        model_name = url_params_validation(self.kwargs)
        sensordata = get_model_by_name(model_name)
        return sensordata.objects.all().order_by('time')

    def get_serializer_class(self):
        model_name = url_params_validation(self.kwargs)
        sensordata = get_model_by_name(model_name)
        serializer_class = sensordata.get_serializer()
        return serializer_class

