from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import SubSerializer
from django.shortcuts import get_object_or_404
from rest_framework import status

class SubscriptionList(APIView):
    def post(self, request):
        user_data = request.data # json -> object (Serializer)
        serializer = SubSerializer(data=user_data)

        serializer.is_valid(raise_exception=True)
        serializer.save(subscriber=request.user)

        return Response(serializer.data, 201)
        
from .models import Subscription
class SubscriptionDetail(APIView):
    def get(self, request, pk):
        # api/v1/sub/{pk} -> 1번 유저가 구독한 사람들의 리스트가 궁금.
        subs = Subscription.objects.filter(subscribed_to=pk) # objects -< json
        serializer = SubSerializer(subs, many=True)

        return Response(serializer.data)


    def delete(self, request, pk):
        sub = get_object_or_404(Subscription, pk=pk, subscriber=request.user)
        sub.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)