from django.db import models
from django.utils.encoding import smart_unicode

# Create your models here.

class SignUp(models.Model):
    Seminar_Title = models.CharField(max_length=120, null=True, blank = True)
    Presenter = models.CharField(max_length=120, null=True, blank = True)
    Date = models.CharField(max_length=120, null=True, blank = True)
    Description = models.CharField(max_length=600, null=True, blank = True)
    Time_Start = models.CharField(max_length=20, null=True, blank = True)
    Time_End = models.CharField(max_length=20, null=True, blank = True)
    Department = models.CharField(max_length=20, null=True, blank = True)
    Your_Email = models.EmailField(null = False, blank = False)
    Password = models.CharField(max_length=20, null=True, blank = True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    talks = models.Manager()
    
    def __unicode__(self):
        return smart_unicode(self.Seminar_Title)
    
    

