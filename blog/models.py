from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
# Create your models here.

class PostModel(models.Model):
    title = models.CharField(max_length = 100)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_create = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='post')
    

    class Meta:
        ordering = ('-date_create',)


    #for comments 
    def comment_count(self):
        return self.comment_set.all().count()#comment_set all is keyword
    
    def comment(self):
        return self.comment_set.all() #display only comments
    
    def __str__(self) :
        return self.title
    


class ProfileModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=100,default='Unknown')
    image = models.ImageField(upload_to='profile_images/', default='media\default.jpg', null=True, blank=True)
    def __str__(self) :
        return self.user.username
    

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(PostModel, on_delete=models.CASCADE)
    content = models.CharField(max_length = 200)

    def __str__(self) :
        return self.content
    
class savecon(models.Model):
    name=models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    message = models.TextField()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs) 