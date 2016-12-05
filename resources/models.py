from django.db import models
 
# Create your models here.

class Tag(models.Model):

    """
     Model for SermonCategory

    """
    name  = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'Sermon categories'

    def __str__(self):
        return self.name

class Sermon(models.Model):

    """
     Model for Sermon
    """
    date_posted = models.DateField(auto_now_add=True)
    date = models.DateField(auto_now_add=False)
    title= models.CharField(max_length=500)
    verse = models.CharField(max_length=100)
    text_verse = models.CharField(max_length=100)
    verse_text = models.TextField()
    content =  models.TextField()
    author = models.CharField(max_length=100)
    categorys = models.ForeignKey(Tag, related_name='sermons')


    def __str__(self):
        return self.title

class Comment(models.Model):

    """
     Model for SermonComment
    """
    sermon = models.ForeignKey(Sermon, related_name='comments')
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=100)
    content =  models.TextField()

    class Meta:
        verbose_name_plural = 'Sermon comments'

    def __str__(self):
        return self.author

class Devotion(models.Model):

    """
     Model for Devotion
    """
    date_posted = models.DateField(auto_now_add=True)
    principle = models.CharField(max_length=1000)
    title= models.CharField(max_length=500)
    content =  models.TextField()
    
    def __str__(self):
        return self.title
 