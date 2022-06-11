from rest_framework import generics
from rest_framework.response import Response

from services.services import JobServiceUtils, UserServiceUtils
from .models import Job
from .serializers import EndJobSerializer, JobSerializer


class JobApiList(generics.ListAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer


class EndJobApi(generics.UpdateAPIView):
    queryset = Job.objects.all()
    serializer_class = EndJobSerializer

    def update(self, request, *args, **kwargs):
        serializer = EndJobSerializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except:
            raise
        validate_data = serializer.validated_data
        is_true_text = JobServiceUtils().is_true_text(validate_data)
        if is_true_text:
            UserServiceUtils().update_balance_user(validate_data, request.user)
        else:
            return Response({'error': 'bad text'}, status=400)

        return Response("asd")
