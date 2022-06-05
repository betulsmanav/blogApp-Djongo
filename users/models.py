from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserProfile(models.Model):
    portfolio = models.URLField(blank=True)
    profile_pic = models.CharField(max_length=500,default="https://media.istockphoto.com/vectors/user-icon-flat-isolated-on-white-background-user-symbol-vector-vector-id1300845620?k=20&m=1300845620&s=612x612&w=0&h=f4XTZDAv7NPuZbG0habSpU0sNgECM0X7nbKzTUta3n8=")
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.username
