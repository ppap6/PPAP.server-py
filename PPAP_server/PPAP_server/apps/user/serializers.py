from django.utils import timezone
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from role.serializers import RoleSerializer
from user.models import User
class UserSerializer(ModelSerializer):
    role = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model= User
        fields = '__all__'
        # write_only_fields= ("password",)
        extra_kwargs ={
            "password":{"write_only":True}
        }
    def create(self, validated_data):
        data = self.context["request"].data
        role_id = int(data["role"])
        try:
            account = validated_data.pop("account")
            password = validated_data.pop("password")
        except:
            raise ValueError('The given account and password must be set')
        return User.objects.create_user(account, password=password,role_id=role_id,**validated_data)

    def update(self, instance, validated_data):
        data = self.context["request"].data
        update_time = timezone.now()
        validated_data["role_id"] = int(data["role"])
        validated_data["update_time"] = update_time
        super().update(instance, validated_data)
        if validated_data.get("password",""):
            instance.set_password(validated_data["password"])
            instance.save()
        return instance

