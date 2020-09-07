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

status = (('Single','Single'),('Single','Single'))

types = (('Fair','Fair'),('Black','Black'),('Brown','Brown'))

bgroup = (('-A','-A'),('B','B'),('AB','AB'),('O','O'))

tongue = (('Assamese','Assamese'),('Bengali','Bengali'),('Bodo','Bodo'),('Dogri','Dogri'),('English','English'),('Gujarati',
                                                                                                                 'Gujarati'),
          ('Hindi','Hindi'),('Kannada','Kannada'),('Kashmiri','Kashmiri'),('Konkani','Konkani'),('Maithili','Maithili'),
          ('Malayalam','Malayalam'),('Marathi','Marathi'),('Meitei (Manipuri)','Meitei (Manipuri)'),('Nepali','Nepali'),
          ('Odia','Odia'),('Punjabi','Punjabi'),('Sanskrit','Sanskrit'),('Santali','Santali'))

income = (('100000','<100000'),('100000-300000','100000-300000'),('300000-600000','300000-600000'),
          ('600000-1000000','600000-1000000'),('1000000-1500000','1000000-1500000'),
          ('1500000-2000000','1500000-2000000'),('>2000000','>2000000'))

religion_choice = (('Hinduism','Hinduism'),('Islam','Islam'),('Christianity','Christianity'),('Sikhism','Sikhism'),
                    ('Buddhism','Buddhism'),('Jainism','Jainism'),('Zoroastrianism','Zoroastrianism'))


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
    user = models.OneToOneField(settings.AUTH_USER_MODEL,blank=True,null=True,on_delete=models.CASCADE)
    age = models.PositiveSmallIntegerField(blank=True,null=True)

    # Bride grooms details
    navaras = models.CharField(max_length=50,blank=True,null=True)
    maritial_status = models.CharField(max_length=50,choices=status,blank=True,null=True)
    height = models.FloatField(blank=True,null=True)
    weight = models.PositiveSmallIntegerField(blank=True,null=True)
    body_type = models.CharField(max_length=20,blank=True,null=True,choices=types)
    birthdate = models.DateTimeField(blank=True,null=True)
    blood_group = models.CharField(max_length=10,blank=True,null=True,choices=bgroup)
    mother_tongue = models.CharField(max_length=30,blank=True,null=True,choices=tongue)
    annual_income = models.CharField(max_length=20,blank=True,null=True,choices=income)
    religion = models.CharField(max_length=30,null=True,blank=True,choices=religion_choice)
    caste = models.CharField(max_length=20,null=True,blank=True)
    sub_caste = models.CharField(max_length=20,blank=True,null=True)
    birthplace = models.CharField(max_length=50,blank=True,null=True)
    occupation = models.CharField(max_length=100,blank=True,null=True)
    occupation_detail = models.CharField(max_length=200,blank=True,null=True)
    education = models.CharField(max_length=100,blank=True,null=True)
    education_detail = models.CharField(max_length=200,blank=True,null=True)

    drink_habbit = models.CharField(max_length=20,blank=True,null=True,choices=types)
    smoke_habbit = models.CharField(max_length=20,blank=True,null=True,choices=types)
    eating_habbits = models.CharField(max_length=100,blank=True,null=True)
    hobbies = models.CharField(max_length=100,blank=True,null=True)

    devak = models.CharField(max_length=100,blank=True,null=True)
    mana = models.CharField(max_length=100,blank=True,null=True)
    nadi = models.CharField(max_length=100,blank=True,null=True)
    rassi = models.CharField(max_length=100,blank=True,null=True)

    father_name = models.CharField(max_length=100,blank=True,null=True)
    father_occupation = models.CharField(max_length=200,blank=True,null=True)
    mother_name = models.CharField(max_length=100,blank=True,null=True)
    brother_count = models.PositiveSmallIntegerField(max_length=3, blank=True)
    sister_count = models.PositiveSmallIntegerField(max_length=3, blank=True)
    uncle_count = models.PositiveSmallIntegerField(max_length=3, blank=True)
    atya_count = models.PositiveSmallIntegerField(max_length=3, blank=True)
    mavasi_count = models.PositiveSmallIntegerField(max_length=3, blank=True)
    other_relatives = models.CharField(max_length=100,blank=True,null=True)

    address_line1 = models.CharField(max_length=200)
    address_line2 = models.CharField(max_length=100,blank=True,null=True)
    city = models.CharField(max_length=100)
    zipcode = models.PositiveIntegerField(max_length=6)
    district = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    current_location = models.CharField(max_length=200)

    agree_tnc = models.BooleanField()

    @property
    def images(self):
        return self.img.all()

    def __str__(self):
        return self.user.username


class ProfileImage(models.Model):
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE,related_name="img")
    image = models.CharField(max_length=10,blank=True,null=True)


# @receiver(post_save,sender=settings.AUTH_USER_MODEL)
# def userprofile_receiver(sender, instance, created, *args, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
#     else:
#         instance.profile.save()





