from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Post Model
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    # creating a relationship between User and Post model
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    # dunder method to specify how the records should be printed out
    def __str__(self):
        return self.title
    
    # function to redirect the user when post is created 
    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})
