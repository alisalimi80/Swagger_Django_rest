from django.db import models 
from django.db.models import PROTECT 
from PIL import Image
from django.contrib.auth.models import User


# Create your models here.

class Writer(models.Model):

    first_name = models.CharField(max_length=120,null=False)

    last_name = models.CharField(max_length=120,null=False)

    birthday = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Cast(models.Model):

    first_name = models.CharField(max_length=120,null=False)

    last_name = models.CharField(max_length=120,null=False)

    birthday = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Movie(models.Model):

    name = models.CharField(max_length=120,null=False)

    time = models.CharField(max_length=120,null=False)

    description = models.TextField(max_length=2000,null=True,blank=True)

    country = models.CharField(max_length=120,null=False)

    language = models.CharField(max_length=120,null=False)

    writer = models.ForeignKey(Writer,on_delete=PROTECT)

    casts = models.ManyToManyField(Cast)

    def __str__(self):
        return self.name

    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, editable= False)
    avatar = models.ImageField(default='default.png', upload_to='profile_images',blank=True)
    bio = models.TextField()

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        super().save()
        img = Image.open(self.avatar.path)
        if img.height > 100 or img.width > 100:
            new_img = (100, 100)
            img.thumbnail(new_img)
            img.save(self.avatar.path)




