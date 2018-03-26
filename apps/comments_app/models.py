# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class CommentManager(models.Manager):
    def Validator(self, postdata):
        results = {'status': True, 'errors': []}
        if len(postdata['comment']) < 3:
            results['errors'].append('comments is too short')
        if postdata['comment'].isspace() == True:
            results['errors'].append('You can not just add spaces Ray')
        if len(results['errors']) > 0:
            results['status'] = False
        return results
class Comment(models.Model):
    comment = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CommentManager()    