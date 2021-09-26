from rest_framework import serializers
from account.models import User

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        # fields = ('userid', 'nickname') # 일부의 필드만 보여줌
        fields = '__all__' # 모든 필드 사용