import datetime

from oneverse.models import Verse
from oneverse_api.serializers import VerseSerializer, CreateVerseSerializer
from rest_framework import generics
from rest_framework import permissions
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response



@api_view(["GET"])
@permission_classes([permissions.AllowAny])
def oneverse_get_one_today(request):
    '''
    Get one verse of the today
    :param request:
    :return:
    '''
    if request.method == "GET":
        today = datetime.datetime.now()
        today_str = "%s-%s-%s" %(today.year, today.month, today.day)
        try:
            verse = Verse.objects.get(push_date = today_str)
            serializer = VerseSerializer(verse, context={'request': request})
            return Response(serializer.data, status = status.HTTP_200_OK)
        except Verse.DoesNotExist:
            return Response({"details":"does not exist"},
                        status= status.HTTP_404_NOT_FOUND)

class ListVerseView(generics.ListAPIView):
    queryset = Verse.objects.all()

    lookup_field = ('id')

    serializer_class = VerseSerializer

    permission_classes = [
        permissions.IsAdminUser
    ]


class CreateVerseView(generics.ListCreateAPIView):
    queryset = Verse.objects.all().order_by("push_date")

    lookup_field = ('id')

    serializer_class = CreateVerseSerializer

    permission_classes = [
        permissions.IsAdminUser
    ]

    def perform_create(self, serializer):

        if serializer.is_valid():
             # The serializer.data property
            # is only valid if you have a saved instance to serializer.
            # Either call serializer.save() or use serializer.validated_data
            # to access date prior to saving.
            push_date = serializer.validated_data["push_date"]

            if not Verse.objects.filter(push_date = push_date).exists():
                serializer.save()
            else:
                return Response({"details":"already created for this date"},
                            status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"details":"already created for this date"},
                            status=status.HTTP_400_BAD_REQUEST)



class UpdateVerseView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Verse.objects.all()

    lookup_field = ('id')

    serializer_class = VerseSerializer

    permission_classes = [
        permissions.IsAdminUser
    ]

    # def get_object(self):
    #     queryset = Verse.objects.all()
    #     filter = {}
    #     today = datetime.datetime.now()
    #     today_str = "%s-%s-%s" %(today.year, today.month, today.day)
    #     filter["push_date"] = today
    #
    #     obj = get_object_or_404(queryset, **filter)
    #     self.check_object_permissions(self.request, obj)
    #     return obj
    #
    # def perform_update(self, serializer):
    #     serializer.save()
    #
    # def perform_destroy(self, instance):
    #     instance.delete()