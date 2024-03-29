from rest_framework import serializers
from .models import Video
from users.serializers import UserSerializer
from comments.serializer import CommentSerializer
from reactions.models import Reaction


class VideoListSerializer(serializers.ModelSerializer):
    # Video:User => Video(FK) -> User
    user = UserSerializer(read_only=True) # 사용자 정보를 직렬화

    class Meta:
        model = Video
        fields = "__all__"

class VideoDetailSerializer(serializers.ModelSerializer):
    # Video:User => Video(FK) -> User
    user = UserSerializer(read_only=True) # 사용자 정보를 직렬화
    # Video:Comment => Video -> comment(FK)
    # - Reverse Accessor
    # - 부모가 자녀를 찾을 때 => _set으로 부모에 속한 자녀들을 모두 찾을 수 있다.
    comments_set = CommentSerializer(many=True, read_only=True)

    reactions = serializers.SerializerMethodField()
    # comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Video
        fields = "__all__"

    def get_reactions(self, video):
        return Reaction.get_video_reaction(video) # 비디오 -> 리액션 가져오기 