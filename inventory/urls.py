from django.conf.urls import url
from .views import item_list
 
 
urlpatterns = [
    url('items/', item_list, name='item-list'),
]