from djoser.serializers import UserSerializer


class CustomUserSerializer(UserSerializer):

    class Meta(UserSerializer.Meta):
        fields = (
            'id',
            'email',
            'username',
            'is_staff',
            )
