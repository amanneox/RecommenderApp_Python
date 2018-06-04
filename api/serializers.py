from rest_framework_mongoengine import serializers
from api.models import *

class CommentSerializer(serializers.DynamicDocumentSerializer):
    content=StringField()
    name=StringField()


class UserSerializer(serializers.DocumentSerializer):
    class Meta:
        model=User
        fields='__all__'
    email=ListField(StringField())
    first_name=ListField(StringField())
    last_name=ListField(StringField())
    number=ListField(IntField())
    social=ListField(StringField())

    def create(self, validated_data):
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.number = validated_data.get('number',instance.number)
        instance.save()
        return instance