from rest_framework import generics, permissions

from .models import Interested
from .serializers import InterestedSerializer
from soundcheck_drf_api.permissions import IsOwnerOrReadOnly


class InterestedListView(generics.ListCreateAPIView):
    """
    List of events the logged in user is interested in
    """
    serializer_class = InterestedSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Interested.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class InterestedDetailView(generics.RetrieveDestroyAPIView):
    """
    Detail view of interested events
    User may delete the event if they are the owner
    """
    serializer_class = InterestedSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Interested.objects.all()