from rest_framework import serializers

from .models import Nft


class NftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nft
        fields = "__all__"


class NftBuySerializer(serializers.Serializer):
    nft_id = serializers.IntegerField()

    def validate(self, attrs):
        nft_id = attrs.get('nft_id')
        if not Nft.objects.filter(pk=nft_id):
            raise
        return attrs
