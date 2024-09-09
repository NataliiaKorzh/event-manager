from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EventViewSet, EventRegistrationViewSet

router = DefaultRouter()
router.register(r"", EventViewSet, basename="event")
router.register(r"event-register", EventRegistrationViewSet, basename="event-register")

urlpatterns = [
    path("", include(router.urls)),
]

app_name = "events"
