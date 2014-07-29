from django.db import models 
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class UserLink(models.Model):
  from_user=models.ForeignKey(User,related_name='fromuser')
  to_user=models.ForeignKey(User,related_name='touser')
  date_added=models.DateField()
  
  def __unicode__(self): #note: 2 underscores on each side
    return self.from_user.username+"is following "+self.to_user.username;
  def save(self,*args, **kwargs):
    if (self.from_user.username==self.to_user.username):
        raise ValidationError("Cannot friend yourself"); #Cannot friend yourself
    else:
        super(UserLink, self).save(*args, **kwargs) # Call the "real" save() method.
  class Meta:
    unique_together = ("from_user","to_user")