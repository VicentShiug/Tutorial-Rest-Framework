from rest_framework import viewsets
from rest.serializers import ToDoSerializer
from rest.models import ToDo
from rest_framework import permissions

class ToDoViewSets(viewsets.ModelViewSet):
    serializer_class = ToDoSerializer
    queryset = ToDo.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]