from rest_framework import serializers

from config.accounts.models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'full_name', 'is_verified']
