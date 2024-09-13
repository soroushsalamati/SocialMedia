from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    user = models.ForeignKey(User, on_delete = models.PROTECT,)
    image = models.ImageField(upload_to='post_image')
    like_count = models.IntegerField(default=0)
    def __str__(self) -> str:
        return self.user.username


class Follow(models.Model):
    user = models.ForeignKey(User, on_delete = models.PROTECT,)
    follow = models.ForeignKey(User, on_delete = models.PROTECT, related_name='follow')
    def __str__(self) -> str:
        return self.user.username


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete = models.PROTECT,)
    post = models.ForeignKey(Post, on_delete = models.PROTECT,)
    comment = models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.user.username
    

class Like(models.Model):
    user = models.ForeignKey(User, on_delete = models.PROTECT,)
    post = models.ForeignKey(Post, on_delete = models.PROTECT,)
    def __str__(self) -> str:
        return self.user.username
