from rest_framework import serializers

from django.contrib.auth import get_user_model


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'first_name', 'last_name', 'username')
        read_only_fields = ('username', )
        extra_kwargs = {'first_name': {'allow_blank': False, 'required': True}}


class FacebookLoginSerializer(serializers.Serializer):
    accessToken = serializers.CharField()