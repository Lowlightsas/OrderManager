from rest_framework import serializers
from .models import Ticket

class TicketStatusUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ['code', 'status']
        