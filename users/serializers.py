from rest_framework import serializers
from django.contrib.auth.models import User

from noticeboard.models import Notice


class UserSerializer(serializers.ModelSerializer):
    notices = serializers.HyperlinkedRelatedField(many=True, queryset=Notice.objects.all(),
                                                  view_name='notice-detail')

    class Meta:
        model = User
        fields = ['id', 'username', 'notices']
