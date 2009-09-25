from django.db import models

class Blog(models.Model):
    author = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateTimeField('date published')
    
    def __unicode__(self):
            return self.title
            
    def was_published_today(self):
            return self.pub_date.date() == datetime.date.today()

class Comment(models.Model):
    blog = models.ForeignKey(Blog)
    author = models.CharField(max_length=200)
    email = models.EmailField()
    comment = models.TextField()
    url = models.URLField()
    pub_date = models.DateTimeField('date published')
    
    def __unicode__(self):
            return self.author
    
    