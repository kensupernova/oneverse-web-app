#coding:utf-8
from gcm import GCM

from oneverse.models import GcmRegister
from oneverse.models import Secret
from rest_framework import permissions
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response


@api_view(["GET", "POST"])
@permission_classes([permissions.AllowAny])
def save_user_gcm_registration_id(request):
    '''
    save user gcm registration id
    :param request:
    :return:
    '''
    if request.method == "GET":

        return Response({"detail": "get is not supported"})
    elif request.method == "POST":

        data = request.data
        deviceId = data["deviceId"]
        gcmToken = data["gcmToken"]

        gcm = GcmRegister.objects.create(deviceId=deviceId, gcmToken=gcmToken)
        gcm.save()

        return Response({"detail": "ok"}, status = status.HTTP_200_OK)

@api_view(["GET", "POST"])
@permission_classes([permissions.IsAdminUser])
def send_gcm(request):
    '''
    save user gcm registration id
    :param request:
    :return:
    '''
    if request.method == "GET":

        return Response({"detail": "get is not supported"})
    elif request.method == "POST":
        secret = Secret.objects.all().order_by('-id')[0]
        API_KEY = secret.api_key
        gcm = GCM(API_KEY)
        ##data = {'param1': 'value1', 'param2': 'value2'}
        data = request.data

        # Downstream message using JSON request
        ##reg_ids = ['token1', 'token2', 'token3']
        tokens = GcmRegister.objects.all()
        reg_ids = []
        for token in tokens:
            reg_ids.append(token.gcmToken)

        response = gcm.json_request(registration_ids=reg_ids, data=data)

        # Downstream message using JSON request with extra arguments
        res = gcm.json_request(
            registration_ids=reg_ids, data=data,
            collapse_key='uptoyou', delay_while_idle=True, time_to_live=3600
        )

        # Topic Messaging
        topic = 'global'
        gcm.send_topic_message(topic=topic, data=data)

        return Response({'detail':res})