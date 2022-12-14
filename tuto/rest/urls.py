from django.urls import path, include
from rest_framework import routers
from rest.views import ToDoViewSets

router = routers.DefaultRouter()
router.register(r'lista', ToDoViewSets, basename='lista')

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))

]
