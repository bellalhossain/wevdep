# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
 
class Category(models.Model):
    name = models.CharField(max_length=50)
 
    def __str__(self):
        return self.name 
 
 
class Item(models.Model):
    name = models.CharField(max_length=150)
    category = models.ForeignKey(Category, on_delete=None)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name

# Create your models here.
