from rest_framework import viewsets
from .models import Hero, Student
from .serializers import HeroSerializers, StudentSerializers
# Create your views here.




class HeroViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.all().order_by('name')
    serializer_class = HeroSerializers


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers




