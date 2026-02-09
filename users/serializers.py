from rest_framework import serializers # pyright: ignore[reportMissingImports]
from django.contrib.auth.models import User

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, data):
        return User.objects.create_user(**data)
