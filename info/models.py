from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import RegexValidator


gender_choices = (
    ('male', 'Male'),
    ('female', 'Female'),

)
relationship_choices = (
    ('son', 'Son'),
    ('daughter', 'Daughter'),
    ('brother', 'Brother'),
    ('sister', 'Sister'),

)


class User(AbstractUser):
    email = models.EmailField(verbose_name='email address',max_length=255,unique=True,blank=True,null=True)
    mobile_no = models.CharField(validators=[
        RegexValidator(
            regex='[1-9]{1}[0-9]{9}',
            message='Number should be 10 digit',
            code='invalid_number'
        ),
    ],max_length=10,blank=True,null=True)
    full_name = models.CharField(max_length=255,blank=True,null=True)
    relation = models.CharField(max_length=10,blank=True,null=True,choices=relationship_choices)
    gender = models.CharField(max_length=6,blank=True,null=True,choices=gender_choices)


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    age = models.IntegerField(blank=True,null=True)

    def __str__(self):
        return self.user.username


@receiver(post_save,sender=settings.AUTH_USER_MODEL)
def userprofile_receiver(sender, instance, created, *args, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    else:
        instance.profile.save()





