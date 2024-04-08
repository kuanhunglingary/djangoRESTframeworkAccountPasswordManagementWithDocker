from rest_framework import serializers
from .models import User

class RegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=32, min_length=3, write_only=True)
    password = serializers.CharField(max_length=32, min_length=8, write_only=True)
    class Meta:
        model = User
        fields = ['username', 'password']

    
class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=32, min_length=3, write_only=True)
    password = serializers.CharField(max_length=32, min_length=8, write_only=True)
    def get_token(self, obj):
        user = User.objects.get(username=obj['username'])
        return {
            'refresh': user.token()['refresh'],
            'access': user.tokens()['access']
        }
    class Meta:
        model = User
        fields = ['username', 'password','token']
