from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Imginfo(models.Model):
    qiniu_url = models.URLField()
    year = models.IntegerField()
    month = models.IntegerField()
    pub_date = models.DateTimeField('创建时间',auto_now_add=True)

    discription = models.CharField(max_length = 200,null=True,blank=True)
    # def __str__(self):
    #     if self.discription != None:
    #         return self.discription

# class UserProfile(models.Model):
#     # This line is required. Links UserProfile to a User model instance.
#     user = models.OneToOneField(User)
#
#     # The additional attributes we wish to include.
#     # website = models.URLField(blank=True)
#     # picture = models.ImageField(upload_to='profile_images', blank=True)
#
#     # Override the __unicode__() method to return out something meaningful!
#     def __str__(self):
#         return self.user.username
