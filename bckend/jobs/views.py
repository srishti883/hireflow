from rest_framework import generics

from .models import Job
from .serializers import JobSerializer
from .permissions import IsHR


class JobListCreateView(generics.ListCreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [IsHR]

    def perform_create(self, serializer):
        serializer.save(posted_by=self.request.user)