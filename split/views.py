from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from split.models import Split
from split.serializer import SplitSerializer


class SplitViewSet(viewsets.ModelViewSet):
    queryset = Split.objects.all()
    serializer_class = SplitSerializer
    permission_classes = [IsAuthenticated]
