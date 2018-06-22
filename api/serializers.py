from rest_framework_mongoengine import serializers
from api.models import *
import json
from api.geocoder import *
from api.models import Post


class AdminLogin(object):
    def admin_auth(self,validated_data):
        x = AdminUser.objects(__raw__={'email': validated_data.get('email'),'password':validated_data.get('password')})

        if not x:
            return False
        else:
            return True


class CommentFilter(object):
    def filter(self,validated_data):
        com_list=([x.comments for x in Post.objects(sid=[validated_data[0]])])
        return com_list


class DataFilter(object):
    def filter(self,validated_data):
        l=list()
        service=Service.objects(__raw__={'category':validated_data.get('category')})
        cat_list=iter([x.id for x in service])
        for i in cat_list:
            item = Item.objects(__raw__={'category':i})
            valid_data =[(x.name, x.location) for x in item]
            x=LocationSerializer.parse(LocationSerializer(),validated_data,valid_data)
            l.append(x)
        return l


class LocationSerializer():

    def parse(self,validated_data,data):
        l=list()
        start = (validated_data.get('lat'), validated_data.get('lng'))
        range=validated_data.get('range')
        it=iter(data)
        for i in it:
            x=dict(i[1])
            end=(x.get('lat'),x.get('lng'))
            if print(Distace.distance(Distace(), start, end, range)):
                print("W")

        return l


class AdminUserSerializer(serializers.DocumentSerializer):
    class Meta:
        model=AdminUser
        fields='__all__'


    def create(self, validated_data):
        return AdminUser.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.password = validated_data.get('password', instance.password)
        instance.usernmae=validated_data.get('username',instance.username)
        instance.save()
        return instance

    def __delete__(self, instance):
        return AdminUser.objects.delete()

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