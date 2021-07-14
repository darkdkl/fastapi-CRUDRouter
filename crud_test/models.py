import ormar
from .db import MainMeta

class Category(ormar.Model):
    id = ormar.Integer(primary_key=True)
    name = ormar.String(max_length=50)

    class Meta(MainMeta):
        pass


class Post(ormar.Model):
    id = ormar.Integer(primary_key=True)
    title = ormar.String(max_length=50)
    text = ormar.String(max_length=4000)
    draft = ormar.Boolean(default=False)
    category = ormar.ForeignKey(Category, related_name='posts')

    class Meta(MainMeta):
        pass


class Comment(ormar.Model):
    id = ormar.Integer(primary_key=True)
    text = ormar.String(max_length=400)
    moderated = ormar.Boolean(default=False)
    post = ormar.ForeignKey(Post, related_name='comments')

    class Meta(MainMeta):
        pass