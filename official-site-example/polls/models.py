from django.db import models
import datetime
from django.utils import timezone

# Create your models here.
class Question(models.Model):
    def was_published_resently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    was_published_resently.admin_order_field = 'pub_date'
    was_published_resently.boolen = True
    was_published_resently.short_description = 'Published recently?'
    def __str__(self):
        return self.question_text

    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Choice(models.Model):
    def __str__(self):
        return self.choice_text

    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
