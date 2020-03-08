# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager)


class BsuClientlist(models.Model):
    code = models.CharField(primary_key=True, max_length=10)
    name = models.CharField(max_length=40, blank=True, null=True)
    addr1 = models.CharField(max_length=40, blank=True, null=True)
    addr2 = models.CharField(max_length=40, blank=True, null=True)
    city = models.CharField(max_length=25, blank=True, null=True)
    state = models.CharField(max_length=15, blank=True, null=True)
    zip = models.CharField(max_length=15, blank=True, null=True)
    email = models.CharField(max_length=40, blank=True, null=True)
    main_phone = models.CharField(max_length=20, blank=True, null=True)
    after_hours_phone = models.CharField(max_length=20, blank=True, null=True)
    ceo_mgr = models.CharField(max_length=40, blank=True, null=True)
    comments = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bsu_clientlist'


class BsuEformsschemadetail(models.Model):
    detailid = models.AutoField(primary_key=True, unique=True)
    loanid = models.IntegerField(blank=True, null=True)
    pageid = models.IntegerField(blank=True, null=True)
    groupid = models.IntegerField(blank=True, null=True)
    lineid = models.IntegerField(blank=True, null=True)
    fieldtype = models.CharField(max_length=10, blank=True, null=True)
    fieldvalue = models.CharField(max_length=2000, blank=True, null=True)
    fieldattr = models.CharField(max_length=3000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bsu_eformsschemadetail'


class BsuEformsschemamaster(models.Model):
    loanid = models.AutoField(primary_key=True, unique=True)
    code = models.CharField(max_length=10, blank=True, null=True)
    loantitle = models.CharField(max_length=50, blank=True, null=True)
    loandesc = models.CharField(max_length=1000, blank=True, null=True)
    lastmodified = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bsu_eformsschemamaster'

class UserManager(BaseUserManager):
    # Only create users through this function
    def create_user(self, username, password):
        if not username:
            raise ValueError('Users must have a user name.')
        if not password:
            raise ValueError('Users must have a password.')

        user = self.model(
            user_name = username
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, passwd):
        user = self.create_user(username, passwd)
        user.is_staff()
        user.is_superuser = True
        user.save()
        return user

class BsuOfficeusers(AbstractBaseUser):
    user_name = models.CharField(primary_key=True, max_length=12)
    failedremain = models.IntegerField(blank=True, null=True)
    forceremain = models.IntegerField(blank=True, null=True)
    priorlogin = models.CharField(max_length=20, blank=True, null=True)
    failedlogin = models.CharField(max_length=20, blank=True, null=True)
    pwchange = models.DateTimeField(blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)

    objects = UserManager()

    USERNAME_FIELD = 'user_name'
    EMAIL_FIELD = 'email'

    REQUIRED_FIELDS = []
    
    class Meta:
        managed = False
        db_table = 'bsu_officeusers'