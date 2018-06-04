from django.db import models

# Create your models here.
from mongoengine import *


class User(Document):
    email = ListField(StringField(required=True))
    first_name = ListField(StringField(max_length=50))
    last_name = ListField(StringField(max_length=50))
    number=ListField(IntField())
    social=ListField(StringField())
    meta = {"db_alias": "default", 'collection': 'user'}


class Comment(EmbeddedDocument):
    content = ListField(StringField())
    name = ListField(StringField(max_length=120))


class Post(Document):
    title = ListField(StringField(max_length=120, required=True))
    author = ListField(ReferenceField(User, reverse_delete_rule=CASCADE))
    tags = ListField(StringField(max_length=30))
    comments = ListField(EmbeddedDocumentField(Comment))
    rating=ListField(FloatField())
    meta = {'allow_inheritance': True}

class TextPost(Post):
    content = StringField()

class ImagePost(Post):
    image_path = StringField()

class LinkPost(Post):
    link_url = StringField()

