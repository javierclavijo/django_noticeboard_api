from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Notice


class NoticeSerializer(serializers.ModelSerializer):
    author = serializers.HyperlinkedRelatedField(many=False, queryset=User.objects.all(),
                                                 view_name='user-detail')

    class Meta:
        model = Notice
        fields = ['id', 'title', 'pub_date', 'exp_date', 'body', 'author']
