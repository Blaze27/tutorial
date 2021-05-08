from .models import Hero, Student
from rest_framework import serializers

class HeroSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hero
        fields = (
            'id',
            'name',
            'alias',
        )

class StudentSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = (
            'id',
            'first_name',
            'last_name',
        )
