from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class CreatePlaylist(models.Model):
    name = models.CharField(max_length=200)
    is_private = models.BooleanField(default=False)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.name + " "+ self.user.username

class AddToPlaylist(models.Model):
    playlist = models.ForeignKey(CreatePlaylist,on_delete=models.CASCADE)
    imdb_id = models.CharField(max_length=100,blank=False)

    def __str__(self):
        return self.imdb_id+ " " + self.playlist.name 