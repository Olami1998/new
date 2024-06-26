from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


STATUS = (
    (0, "Draft"),
    (1, "Publish")
)

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    content = models.TextField()
    images = models.FileField(upload_to='images',blank=True, null=True)
    author = models.ForeignKey(User, null=True, blank=True, on_delete= models.CASCADE)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=1)
    
    class meta:
        ordering = ['-created_on']
        
    def __str__(self):
        return self.title
    
    
    
class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)
    
