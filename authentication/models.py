from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass
# Create your models here.



# class   Product(models.Model):
#     name = models.CharField(max_length=100)
#     price = models.PositiveIntegerField(default=0)
#     description = models.TextField()


# class   Notification(models.Model):
#     title = models.CharField(max_length=100)
    
#     class   NotifType(models.TextChoices):
#         FRIEND = 'Friend', 'Friend'
#         CHAT = 'chat', 'chat'
#         TOUR = 'tour', 'tour'
#         MATCH = 'match', 'match'
    
#     notif_type = models.CharField(max_length=20, choices=NotifType.choices, default=NotifType.FRIEND)

#     def __str__(self) -> str:
#         return str(self.title)
    
    