from rest_framework import serializers
from .models import Event, EventRegistration


class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = ["id", "title", "description", "date", "location", "organizer"]


class EventRegistrationSerializer(serializers.ModelSerializer):

    class Meta:
        model = EventRegistration
        fields = ["event", "user"]
