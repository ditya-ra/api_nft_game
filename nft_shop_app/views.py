from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from services.services import NftServiceUtils
from .models import Nft
from .serializers import NftBuySerializer, NftSerializer


class NftApiList(generics.ListAPIView):
    queryset = Nft.objects.all()
    serializer_class = NftSerializer


class NftBuyApi(generics.UpdateAPIView):
    queryset = Nft.objects.all()
    serializer_class = NftBuySerializer
    permission_classes = (IsAuthenticated,)

    def update(self, request, *args, **kwargs):
        serializer = NftBuySerializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except:
            raise
        validate_data = serializer.validated_data
        is_buy_nft = NftServiceUtils().is_buy_nft(request.user, validate_data)
        if is_buy_nft:
            NftServiceUtils.buy_nft(request.user, validate_data)

        return Response('True')
