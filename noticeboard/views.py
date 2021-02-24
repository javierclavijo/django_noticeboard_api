from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .permissions import IsOwnerOrReadOnly
from .serializers import NoticeSerializer
from .models import Notice
from rest_framework import viewsets


class NoticeViewSet(viewsets.ModelViewSet):
    queryset = Notice.objects.all()
    serializer_class = NoticeSerializer
    permission_classes = [IsOwnerOrReadOnly, IsAuthenticatedOrReadOnly]
