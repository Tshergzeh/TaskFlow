from rest_framework import serializers

from config.accounts.models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'full_name', 'is_verified']

class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'full_name', 'password')
        extra_kwargs = {'password': {'write_only': True}}
        
    def create_user(self, user_data):
        user = User.objects.create_user(**user_data)
        return user
    