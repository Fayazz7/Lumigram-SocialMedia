from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Create your models here.


class Post(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="post")
    image = models.ImageField(upload_to="posts", null=True, blank=True)
    caption = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.caption


class UserProfile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="profile")
    display_name = models.CharField(max_length=200, null=True, blank=True)
    about = models.CharField(max_length=200, null=True, blank=True)
    user_pic = models.ImageField(
        upload_to="profiles", default="profile.jpg", null=True, blank=True)
    followers = models.ManyToManyField(
        User, null=True, blank=True, related_name="followers")
    following = models.ManyToManyField(
        User, null=True, blank=True, related_name="following")
    saved = models.ManyToManyField(
        Post, null=True, blank=True, related_name="saved")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username


class Like(models.Model):
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="likes")
    post = models.ForeignKey(
        Post, on_delete=models.DO_NOTHING, related_name="post_like")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.post.caption


class Comment(models.Model):
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="comments")
    post = models.ForeignKey(
        Post, on_delete=models.DO_NOTHING, related_name="post_comment")
    text=models.CharField(max_length=200,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.text


class Stories(models.Model):
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="story")
    text = models.CharField(max_length=200)
    story_image = models.ImageField(upload_to="user-story")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.owner.username


def create_profile(sender, created, instance, **kwargs):
    if created and not instance.is_superuser:
        UserProfile.objects.create(user=instance)


post_save.connect(create_profile,sender=User)
