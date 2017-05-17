import json
import uuid
from django.contrib.auth import authenticate, login, logout, get_user
from django.shortcuts import render
from rest_framework import permissions, viewsets, status, views
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist

import monitor.logging
from authentication.models import Account
from authentication.permissions import IsAccountOwner
from authentication.serializers import AccountSerializer
from sensor.models import *

class AccountViewSet(viewsets.ModelViewSet):
    lookup_field = 'username'
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.AllowAny(),)

        if self.request.method == 'POST':
            return (permissions.AllowAny(),)

        return (permissions.IsAuthenticated(), IsAccountOwner(),)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            Account.objects.create_user(**serializer.validated_data)

            return Response(serializer.validated_data, status=status.HTTP_201_CREATED)

        return Response({
            'status': 'Bad request',
            'message': 'Account could not be created with received data.',
        }, status=status.HTTP_400_BAD_REQUEST)


class LoginView(views.APIView):
    renderer_classes = (JSONRenderer, )
    @csrf_exempt
    def post(self, request, format=None):
        data = json.loads(request.body)

        email = data.get('email', None)
        password = data.get('password', None)

        account = authenticate(email=email, password=password)

        if account is not None:
            if account.is_active:
                login(request, account)

                serialized = AccountSerializer(account)

                return Response(serialized.data)
            else:
                return Response({
                    'status': 'Unauthorized',
                    'message': 'This account has been disabled.'
                }, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({
                'status': 'Unauthorized',
                'message': 'Username/password combination invalid.'
            }, status=status.HTTP_401_UNAUTHORIZED)


class LogoutView(views.APIView):
    permission_classes = (permissions.IsAuthenticated,)

    @csrf_exempt
    def post(self, request, format=None):
        logout(request)
        return Response({}, status=status.HTTP_204_NO_CONTENT)


class OccupyView(views.APIView):
    permission_classes = (permissions.IsAuthenticated,)
    @csrf_exempt
    def post(self, request, format=None):
        data = json.loads(request.body)
        
        #check args
        email = data.get('email', None)
        if email is None:
            return Response({
                'status': 'Unauthorized',
                'message': 'Missing email.'
            }, status=status.HTTP_401_UNAUTHORIZED)
        raw_beacon = data.get('beacon_id', None)
        if raw_beacon is None:
            return Response({
                'status': 'Unauthorized',
                'message': 'Missing beacon_id.'
            }, status=status.HTTP_401_UNAUTHORIZED)

        #check request.user for 
        if not request.user.is_authenticated:
            return Response({
                'status': 'Unauthorized',
                'message': 'User not authenticated, please log in.'
            }, status=status.HTTP_401_UNAUTHORIZED)

        beacon_uuid = uuid.UUID(raw_beacon)
        try:
            spot = spot_data.objects.get(uuid=beacon_uuid)
        except ObjectDoesNotExist as den:
		    return Response({
                        'status':'Unauthorized',
                        'message':'Invalid beacon UUID.'
            }, status=status.HTTP_401_UNAUTHORIZED)

        #user is authenitcated and we have the beacon's spot_data,
        # add this user as the occupant
        #if spot.occ_status is True:
        spot.occupant = request.user
        spot.occ_status = 1
        spot.save()

        #log the occupancy
        monitor.logging.log_occupancy(spot, request.user)

        return Response({
            'status':'Success',
            'structure': ('') if (spot.section.structure is None) else (str(spot.section.structure.name)),
            'section': str(spot.section),
            'number': str(spot.number),
            'rate': spot.section.get_current_rate()
        }, status=status.HTTP_200_OK)
