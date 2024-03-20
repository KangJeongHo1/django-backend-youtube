from rest_framework import serializers
from .models import Video
from users.serializers import UserSerializer


class VideoSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True) # 사용자 정보를 직렬화

    class Meta:
        model = Video
        fields = "__all__"