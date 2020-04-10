from rest_framework.generics import ListCreateAPIView

from app.models import Check
from app.serializers import CheckSerializer


class CheckView(ListCreateAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Check.objects.all().order_by('-created')
    serializer_class = CheckSerializer
