from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from rest_framework import viewsets
from .models import QueryLog
from .serializers import APILogSerializer

from .gemini_sdk import tone_and_intent_analyzer

@api_view(['POST'])
def suggestion(request):
    if not request.data.get("query"):
        return Response(f"not enough field {request.POST}", status=status.HTTP_400_BAD_REQUEST)
    # RUN THE QUERY
    return Response(tone_and_intent_analyzer(request.data.get("query")), status=status.HTTP_200_OK)

class APILogViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = QueryLog.objects.all().order_by('-created_at')
    serializer_class = APILogSerializer
