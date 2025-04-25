from django.db import models

# Create your models here.

class members_invited(models.Model):
    invitation_id = models.CharField(max_length=100)
    inviter_memberid = models.CharField(max_length=100)
    CODE = models.IntegerField()
    INVITED_ADDRESS = models.CharField(max_length=100)
    INVITED_EMAIL = models.CharField(max_length=100)

class member(models.Model):
    member_username = models.CharField(max_length=100,default="SS&CO.")
    member_Memberid = models.CharField(max_length=100)
    member_email = models.EmailField(max_length=100)
    member_address = models.CharField(max_length=100)
    member_phone = models.CharField(max_length=100)

class admins(models.Model):
    admin_id = models.CharField(max_length=20)
    admin_pass = models.CharField(max_length=20)



