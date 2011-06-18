from django.contrib.auth.models import User
from django.db import models, connection
from django.template.defaultfilters import slugify
from django.utils.translation import ugettext_lazy as _
from datetime import datetime

class Story(models.Model):
    """ The Story Object """
    key = models.CharField(max_length=100)
    title = models.CharField(blank=True, max_length=200)
    content = models.TextField(blank=True)
    parent = models.ManyToManyField('self', symmetrical=False, blank=True, null=True, related_name="story_parent")
    child = models.ManyToManyField('self', symmetrical=False, blank=True, null=True, related_name="story_child")
    editorial_alpha = models.BooleanField(default=False)
    science_alpha = models.BooleanField(default=False)
    editorial_beta = models.BooleanField(default=False)
    science_beta = models.BooleanField(default=False)
    editorial_gold = models.BooleanField(default=False)
    science_gold = models.BooleanField(default=False)
    slug = models.CharField(max_length=200, unique=True)
    created = models.DateTimeField(_('created'), default=datetime.now, blank=True)
    modified = models.DateTimeField(_('modified'), blank=True)
    
    class Meta:
        ordering = ('key',)
        verbose_name = _('Story')
        verbose_name_plural = _('Stories')
    
    def save(self, force_insert=False, force_update=False):
        self.modified = datetime.now()
        super(Story, self).save(force_insert, force_update)
    
    def __unicode__(self):
        return self.slug
        
    @models.permalink
    def get_absolute_url(self):
        return ('story_detail', (), {'slug': self.slug})