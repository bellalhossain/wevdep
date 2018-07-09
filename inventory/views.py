# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from .models import Item
 
def item_list(request):
    all_items = Item.objects.all()
    context = {'all_items':all_items}
    return render(request, 'inventory/item_list.html', context)
# Create your views here.
