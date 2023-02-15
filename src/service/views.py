from rest_framework import status
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView


class HealthProbeView(APIView):

    renderer_classes = [JSONRenderer]
    payload = {'ping': 'pong'}

    def get(self, request, *args, **kwargs):
        return Response(data=self.payload, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        return Response(data=self.payload, status=status.HTTP_202_ACCEPTED)
