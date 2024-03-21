from django.db import models
from common.models import CommonModel
from users.models import User
from videos.models import Video

# - User:FK
# - Video:FK
# - like
# - dislike
# - content

class Comments(CommonModel):
    content = models.TextField()
    like = models.PositiveIntegerField(default=0)
    dislike = models.PositiveIntegerField(default=0)

    # User:Comment => 1:N
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # Video:Comment(FK) => 1:N
    # video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name='comments')
    video = models.ForeignKey(Video, on_delete=models.CASCADE)

    