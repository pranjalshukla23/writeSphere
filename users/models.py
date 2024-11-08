from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.

#Profile model
class Profile(models.Model):
    # creating a one-to-one relationship between User and Profile model
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # create an image field, specify the default image and name of the folder to store the images
    image = models.ImageField(default="default.jpg", upload_to="profile_pics")
    
    #dunder method to specify how the records should be displayed
    def __str__(self):
        return f'{self.user.username} Profile'
    
    # overriding the save method of profile
    def save(self):
        super().save()
        
        img = Image.open(self.image.path)
        
        if img.height > 300 or img.width > 300:
            # resize the image to 300x300
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save()
        
        