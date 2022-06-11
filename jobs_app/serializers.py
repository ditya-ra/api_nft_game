from rest_framework import serializers

from .models import Job


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ['id', 'text']


class EndJobSerializer(serializers.Serializer):
    job_id = serializers.IntegerField()
    text = serializers.CharField()

    def validate(self, attrs):
        job_id = attrs.get('job_id')

        if not Job.objects.filter(pk=job_id):
            raise
        return attrs
