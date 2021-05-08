from django.urls import path, include
from rest_framework import routers

from . import views



router = routers.DefaultRouter()
router.register(r'heroes', views.HeroViewSet)
router.register(r'students', views.StudentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]