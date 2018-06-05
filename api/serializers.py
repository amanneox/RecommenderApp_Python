from rest_framework_mongoengine import serializers
from api.models import *

class ServiceSerializer(serializers.DocumentSerializer):
    class Meta:
        model=Service
        fields='__all__'

    def create(self, validated_data):
        return Service.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.category = validated_data.get('category', instance.category)
        instance.subcategory = validated_data.get('subcategory', instance.subcategory)
        instance.status = validated_data.get('status', instance.status)
        instance.save()
        return instance

    def __delete__(self, instance):
        return Service.objects.delete()

class CommentSerializer(serializers.DocumentSerializer):
    class Meta:
        model=Comment
        fields='__all__'

    def create(self, validated_data):
        return Comment.objects.create(**validated_data)


    def update(self, instance, validated_data):
        instance.content = validated_data.get('content', instance.content)
        instance.name = validated_data.get('name',instance.name)
        instance.save()
        return instance

    def __delete__(self, instance):
        return Comment.objects.delete()

class PostSerializer(serializers.DocumentSerializer):
    class Meta:
        model=Post
        fields='__all__'

    def create(self, validated_data):
        return Post.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.author = validated_data.get('author', instance.author)
        instance.tags = validated_data.get('tags', instance.tags)
        instance.comment = validated_data.get('comment',instance.comment)
        instance.rating = validated_data.get('rating',instance.rating)
        instance.save()
        return instance

    def __delete__(self, instance):
        return Post.objects.delete()


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

    def __delete__(self, instance):
        return User.objects.delete()