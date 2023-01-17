from django.contrib import admin
from .models import *
# Register your models here.


database = [ItemA,ItemB,MyAccount,Student,One,two]

admin.site.register(database)
