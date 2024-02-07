from rest_framework import generics, permissions
from soundcheck_drf_api.permissions import IsOwnerOrReadOnly
from likes.models import Check
from likes.serializers import CheckSerializer


class CheckList(generics.ListCreateAPIView):
    """
    A class to list likes or create a like if logged in.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = CheckSerializer
    queryset = Check.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CheckDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve or delete  a like by id.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = CheckSerializer
    queryset = Check.objects.all()
