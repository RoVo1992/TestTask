from django.shortcuts import render
from rest_framework import generics
from rest_framework import viewsets, permissions
from .models import *
from .serializers import *


class TicketViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
