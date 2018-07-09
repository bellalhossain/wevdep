# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib import admin

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField(max_length=10) 
    date_created = models.DateField(verbose_name="Created on date", auto_now_add="True")

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message', 'date_created')