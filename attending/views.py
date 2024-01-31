from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend

from .models import Attending
from .serializers import AttendingSerializer
from soundcheck_drf_api.permissions import IsOwnerOrReadOnly


class AttendingListView(generics.ListCreateAPIView):
    """
    List view of all events the user is attending
    """
    serializer_class = AttendingSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Join.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['event']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class AttendingDetailView(generics.RetrieveDestroyAPIView):
    """
    Detailed view of events that a user is attending
    """
    permission_classes = [IsUserOrReadOnly]
    serializer_class = AttendingSerializer
    queryset = Attending.objects.all()