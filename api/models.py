from django.db import models

# Create your models here.
from mongoengine import *
class AdminUser(Document):
    username=StringField()
    email=StringField(required=True)
    password=StringField(required=True)

class Service(Document):
    name=StringField(max_length=20,required=True)
    category=StringField(required=True)
    subcategory=StringField(required=True)
    status=BooleanField(required=True)




class Item(Document):
    name=StringField(required=True)
    category=ReferenceField(Service)
    img_url=StringField()
    location=DictField()
    address=StringField()
    value=StringField()
    rating=FloatField()



class User(Document):
    email = StringField(required=True)
    first_name = StringField(max_length=50)
    last_name = StringField(max_length=50)
    number=IntField()
    social=ListField(StringField())
    meta = {"db_alias": "default", 'collection': 'user'}



class Post(Document):
    title = StringField(max_length=120, required=True)
    author = ReferenceField(User, reverse_delete_rule=CASCADE)
    tags = ListField(StringField(max_length=30))
    comments = ListField(StringField())
    rating=ListField(FloatField())
    sid=ReferenceField(Service,required=True)
    meta = {'allow_inheritance': True}

class TextPost(Post):
    content = StringField()

class ImagePost(Post):
    image_path = StringField()

class LinkPost(Post):
    link_url = StringField()
