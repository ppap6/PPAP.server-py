from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from role.models import Role
class RoleSerializer(ModelSerializer):
    class Meta:
        model= Role
        fields = '__all__'
        # write_only_fields= ("password",)
        extra_kwargs ={
            "password":{"write_only":True}
        }

    # def create(self, validated_data):
    #     return User.objects.create_user(**validated_data)
    #
    # def update(self, instance, validated_data):
    #     super().update(instance, validated_data)
    #     instance.set_passwoed(validated_data["password"])
    #     instance.save()
    #     return instance

