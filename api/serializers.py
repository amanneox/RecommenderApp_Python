from rest_framework_mongoengine import serializers
from api.models import *

class LocationSerializer():

    def parse(self,validated_data):
        item=Item.objects()
        x=[x.location for x in item if x.name==['Pizza Hut']]
        return True


class ItemSerializer(serializers.DocumentSerializer):
    class Meta:
        model=Item
        fields='__all__'


    def create(self, validated_data):
        return Item.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.category = validated_data.get('category', instance.category)
        instance.location=validated_data.get('location',instance.location)
        instance.address=validated_data.get('address',instance.address)
        instance.img_url=validated_data.get('img_url',instance.img_url)
        instance.save()
        return instance

    def __delete__(self, instance):
        return Item.objects.delete()



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
        instance.comments = validated_data.get('comments',instance.comments)
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