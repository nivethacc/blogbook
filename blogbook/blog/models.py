from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    #find the location for particular post. Not redirect() but reverse() is used.
    #Redirect will direct you to the specific route but reverse() will return you to the
       #route as a string
    #return URL as a string and view will handle it for us.
    #tell django to find any instance to a post
    #post-detail->redirect path,kwargs:got to post with that pk
    def get_absolute_url(self):
        return reverse('post-detail',kwargs={'pk': self.pk})