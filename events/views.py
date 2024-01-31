from rest_framework import generics, permissions, filters
from django.db.models import Count
from django_filters.rest_framework import DjangoFilterBackend

from .models import Event
from .serializers import EventSerializer
from pp5_api.permissions import IsUserOrReadOnly


class EventsList(generics.ListCreateAPIView):
    """
    List events or create an event if logged in
    The perform_create method associates the event with the logged in user.
    """
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Event.objects.annotate(
        comments_count=Count('comment', distinct=True)
    ).order_by('-created_at')

    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = {
        'owner__followed__owner__profile': ['exact'],
        'owner__profile': ['exact'],
        'event_start': ['lte'],
    }
    search_fields = [
        'owner__username',
        'title',
        'event_start',
    ]
    ordering_fields = [
        'comments_count',
        'event_start',
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)