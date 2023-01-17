from django.db import models
from django.contrib.auth.models import User
from django.db.models import Q

# Create your models here.

class Common(models.Model):
    title = models.CharField(max_length=225)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ['title']
        # get_latest_by = 'created' # ---> get_latest_by means recent data is create then data show on top 

    def __str__(self) -> str:
        return self.title


class ItemA(Common):
    content = models.TextField()



class ItemB(Common):
    name = models.CharField(max_length=40)

    class Meta(Common.Meta):     #-----> Inheriate the Common model with Meta class
        ordering = ['-created']    #---> order the deascending created field
        verbose_name = "ITEM B"     #--> Change the name of db  but one is problem S is add automatically so thats' why use verbose_name_plural
        verbose_name_plural = "Item B"  #-->  verbose_name_plural through not add S extra
        app_label = "app" #---> enter app name next developer know that which app model


class MyAccount(User):
    class Meta:
        ordering = ['username']
        proxy = True #---> proxy provide user inheriate data -- simple words aa user da sara data MyAccounts db show krda hai


class Student(Common):
    home_group = models.CharField(max_length=5)

    class Meta:
        constraints = [
            models.CheckConstraint(check=Q(home_group__gte='home'),name='home_group_gte_18')
        ]

