from django.db import models

class Author(models.Model):
  name = models.CharField(max_length=30)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True, auto_now_add=True)

  def __unicode__(self):
    return u'%s' %(self.name)

  class Meta:
    db_table = "authors"