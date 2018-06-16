from django.db import models

# Create your models here.
from mongoengine import *

class Service(Document):
    name=ListField(StringField(max_length=20,required=True))
    category=ListField(StringField(required=True))
    subcategory=ListField(StringField(required=True))
    status=ListField(BooleanField(required=True))




class Item(Document):
    name=ListField(StringField(required=True))
    category=ListField(ReferenceField(Service))
    img_url=ListField(StringField())
    location=ListField(DictField())
    address=ListField(DictField())
    value=ListField(StringField())
    rating=ListField(FloatField())



class User(Document):
    email = ListField(StringField(required=True))
    first_name = ListField(StringField(max_length=50))
    last_name = ListField(StringField(max_length=50))
    number=ListField(IntField())
    social=ListField(StringField())
    meta = {"db_alias": "default", 'collection': 'user'}



class Post(Document):
    title = ListField(StringField(max_length=120, required=True))
    author = ListField(ReferenceField(User, reverse_delete_rule=CASCADE))
    tags = ListField(StringField(max_length=30))
    comments = ListField(StringField())
    rating=ListField(FloatField())
    sid=ListField(ReferenceField(Service,required=True))
    meta = {'allow_inheritance': True}

class TextPost(Post):
    content = StringField()

class ImagePost(Post):
    image_path = StringField()

class LinkPost(Post):
    link_url = StringField()
