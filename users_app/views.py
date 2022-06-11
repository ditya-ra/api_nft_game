from rest_framework import generics
from rest_framework.response import Response

from services.services import UserServiceUtils


class LevelUpdateApiView(generics.ListAPIView):
    queryset = None

    def get(self, request, *args, **kwargs):
        UserServiceUtils().update_level(request.user)
        return Response('asd')
