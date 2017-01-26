from django import forms
from django.forms import ModelForm
from gallery.models import Imginfo
from django.contrib.auth.models import User

class ImgForm(forms.ModelForm):
    qiniu_url = forms.URLField()
    year = forms.IntegerField(initial = 2016)
    month = forms.IntegerField(initial = 1)
    # pub_date = models.DateTimeField('创建时间',auto_now_add=True)

    discription = forms.CharField(max_length = 200,help_text = "Brief discription!")
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Imginfo
        fields = ('qiniu_url','year','month','discription')

class UserForm(forms.ModelForm):
    password = forms.CharField()

    class Meta:
        model = User
        fields = ('username', 'password')
