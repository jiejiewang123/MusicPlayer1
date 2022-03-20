from django.db import models

# Create your models here.
class Song(models.Model):
    title= models.TextField()
    artist= models.TextField()
    image= models.ImageField()
    audio_file = models.FileField(blank=True,null=True)
    audio_link = models.CharField(max_length=200,blank=True,null=True)
    duration=models.CharField(max_length=20)
    paginate_by = 2
    lyrics = models.TextField(default= "This is Lyrics")

    def __str__(self):
        return self.title


class UserAccount(models.Model):
    username = models.TextField(default="good")
    password = models.TextField(default="bad")

    def __str__(self):
        return self.username
