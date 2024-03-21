from django.db import models
from common.models import CommonModel
from users.models import User

# - User:FK => subscriber (내가 구독한 사람)
# - USER:FK => subcribed_to (나를 구독한사람)

# User:Subscription => User(subscriber) =< subscriber, subscriber, subscriber (O)
# User:Subscription => User(subscribed_to) =< subscriber, subscriber, subscriber 


class Subscription(CommonModel):
    subscriber = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subscriptions')
    subscribed_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subscribers')