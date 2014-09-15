from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=400)
    body = models.TextField()
    pub_date = models.DateTimeField('date published')
    
    def __unicode__(self):
        return self.title