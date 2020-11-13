'''Module for views'''
from rest_framework.authentication import BasicAuthentication
from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import api_view
from rest_framework.decorators import authentication_classes
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Username


@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def username(request):
    '''Returns a username that has not been used'''
    obj = Username.objects.first()
    if obj is None:
        return Response({
            'detail': 'No username available.'
        }, status=400)
    obj.delete()
    return Response({'username': obj.username})
