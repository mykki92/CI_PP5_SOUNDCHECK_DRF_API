from rest_framework import generics, permissions
from soundcheck_drf_api.permissions import IsOwnerOrReadOnly
from .models import Follower
from .serializers import FollowerSerializer


class FollowerList(generics.ListCreateAPIView):
    """
    A class to list followers.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Follower.objects.all()
    serializer_class = FollowerSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class FollowerDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve or delete (unfollow) a follower
    """
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Follower.objects.all()
    serializer_class = FollowerSerializer