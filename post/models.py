from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=20, null=False)
    content = models.TextField(max_length=256, null=False)
    image = models.ImageField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    username = models.ForeignKey('user.User', on_delete=models.CASCADE)
    book_mark = models.ManyToManyField('user.User', related_name="book_mark", blank=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    content = models.TextField(max_length=256, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey('user.User', on_delete=models.CASCADE)
    post = models.ForeignKey('post.Post', on_delete=models.CASCADE)


class Like(models.Model):
    user = models.ForeignKey('user.User', on_delete=models.CASCADE)
    post = models.ForeignKey('post.Post', on_delete=models.CASCADE)
