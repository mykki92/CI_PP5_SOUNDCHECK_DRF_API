from rest_framework import generics, permissions
from soundcheck_drf_api.permissions import IsOwnerOrReadOnly
from checks.models import Check
from checks.serializers import CheckSerializer


class CheckList(generics.ListCreateAPIView):
    """
    A class to list checks or create a check if logged in.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = CheckSerializer
    queryset = Check.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CheckDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve or delete a check by id.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = CheckSerializer
    queryset = Check.objects.all()
