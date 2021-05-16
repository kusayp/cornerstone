from django.db import models


# Create your models here.

class Category(models.Model):
    """
     Model for Category

    """
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Hymn(models.Model):
    """
     Model for Hymn

    """
    name = models.CharField(max_length=200)
    # slug = models.CharField(max_length=200, blank=True, null=True)
    has_refrain = models.BooleanField(default=False)
    refrain = models.CharField(max_length=1000, blank=True, null=True)
    categorys = models.ManyToManyField(Category,
                                       related_name='categorys',
                                       blank=True, default=None)

    class Meta:
        verbose_name_plural = 'Hymns'

    def __str__(self):
        return self.name


class Stanza(models.Model):
    """
     Model for Stanza

    """
    content = models.TextField()
    hymn = models.ForeignKey(Hymn, related_name='stanzas', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Stanzas'

    def __str__(self):
        return self.content
