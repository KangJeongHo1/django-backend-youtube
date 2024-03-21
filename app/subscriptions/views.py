from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import SubSerializer

class SubscriptionList(APIView):
    def post(self, request):
        user_data = request.data # json -> object (Serializer)
        serializer = SubSerializer(data=user_data)

        serializer.is_valid(raise_exception=True)
        serializer.save(subscriber=request.user)

        return Response(serializer.data, 201)
        

class SubscriptionDetail(APIView):
    def get(self, request):
        pass

    def delete(self, request):
        pass