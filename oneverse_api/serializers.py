from oneverse.models import Verse
from rest_framework import serializers


class CreateVerseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Verse
        fields = ("id",  "push_date", "verse", "source", "detail")

    def create(self, validated_data):
        obj = Verse.objects.create(**validated_data)
        obj.save()
        return obj

class VerseSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Verse

        extra_kwargs = {
            'url': {'view_name': 'verse-detail', 'lookup_field': 'id'}
        }
        fields = ("id", 'url', "push_date", "verse", "source", "detail")
