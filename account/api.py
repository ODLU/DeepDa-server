from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *

# 모든 유저 관리하는 클래스
class UserList(APIView):
    def get(self, request):
        model=User.objects.all()
        serializer = UserSerializer(model, many=True)
        return Response(serializer.data)