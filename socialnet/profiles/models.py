from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.


class UserProfile(models.Model):
    first_name = models.CharField(_('first name'), max_length=30)
    last_name = models.CharField(_('last name'), max_length=30)

    class Meta:
        verbose_name = 'user profile'
        verbose_name_plural = 'user profiles'

    def get_absolute_url(self):
        return 'profile/{0}/' % self.id

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        "Returns the short name for the user."
        return self.first_name

    def __unicode__(self):
        return '{0} {1}'.format(self.first_name, self.last_name)
