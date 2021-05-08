from django.db import models
from datetime import datetime
from django.urls import reverse
from taggit.managers import TaggableManager
from ckeditor.fields import RichTextField
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=250)
    # content = models.TextField()
    content = RichTextField(blank=True, null=True)
    publish = models.DateTimeField(default=datetime.now())
    tags = TaggableManager()
    heroImage = models.ImageField()
    prevPost = models.ForeignKey(
        'self', related_name='previous_post', on_delete=models.SET_NULL, blank=True, null=True)
    nextPost = models.ForeignKey(
        'self', related_name='next_post', on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post', args=[self.id, self.slug])


class Comment(models.Model):
    name = models.CharField(max_length=25)
    body = models.TextField()
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return f'Comment by {self.name} on {self.post}'
