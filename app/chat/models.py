from django.db import models
from common.models import CommonModel

class ChatRoom(CommonModel):
    # Room과 Message를 따로 관리하는 이유
    # 확장성의 용이 
    name = models.CharField(max_length=100)

class ChatMessage(CommonModel):
    # 정보통신법 3개월 채팅 보관
    # SET_NULL - sender null 값으로 두겠다는 뜻. 1번 > 계정삭제 > null
    sender = models.ForeignKey("users.User", on_delete=models.SET_NULL, null=True) # 알수없음
    message = models.TextField()
    room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)



# User:Msg => 1:N
#   - User: Msg, Msg, Msg => O
#   - Msg: User, User, User => X
    
# Room(부모) - Message(자녀)
# Room:Msg => 1:N
#   - Room: Msg, Msg, Msg => O
#   - Msg: Room, Room, Room => X
