from django.db import models
from django.utils import timezone
<<<<<<< HEAD
from django.contrib.auth.models import BaseUserManager
=======

>>>>>>> feeb9c499d6f816489ba78329921857f70b6c57f

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
<<<<<<< HEAD

class UserManager(BaseUserManager):
    def create_superuser(username,email,password):
        user=self.model(
            username=username,
            email=email,
            is_staff=True,
            is_superuser=True,
            is_active=True,
            )
        user.set_password(password)
        user.save()
        return user 

=======
>>>>>>> feeb9c499d6f816489ba78329921857f70b6c57f
