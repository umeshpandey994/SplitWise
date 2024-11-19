from rest_framework import viewsets

from split.models import Split
from split.serializer import SplitSerializer


class SplitViewSet(viewsets.ModelViewSet):
    queryset = Split.objects.all()
    serializer_class = SplitSerializer
