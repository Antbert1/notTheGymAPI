from rest_framework import serializers

from .models import Classdetail

class ClassdetailSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Classdetail
        fields = ('name', 'type', 'tags', 'blurb')
