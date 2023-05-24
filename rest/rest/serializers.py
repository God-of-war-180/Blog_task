from djoser.serializers import UserCreateSerializer

#we created this class in order to customize getting user credentials in order to create a user profile
class UserSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        fields = ["id","username","email","password"]
