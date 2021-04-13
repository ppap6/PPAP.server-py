# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
import random

from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.contrib.auth.models import  AbstractBaseUser,AbstractUser

# class Test(models.Model):
#     id = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'test'
from django.utils import timezone

from role.models import Role


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, account, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if not account:
            raise ValueError('The given username must be set')
        account = self.model.normalize_username(account)
        user = self.model(account=account, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, account, password=None, **extra_fields):
        extra_fields.setdefault('gender', 0)
        extra_fields.setdefault('role_id', 5)
        extra_fields.setdefault('user_name', "user"+ str(random.randint(1,10000)))
        return self._create_user(account, password, **extra_fields)

class User(AbstractBaseUser):
    GENDER_CHOICES = ((0, 'unknow'), (1, 'female'), (2, 'male'))

    account = models.CharField(max_length=20, blank=True, null=True, unique=True)
    email = models.CharField(max_length=20, blank=True, null=True)
    gender = models.SmallIntegerField(choices=GENDER_CHOICES, default=0, verbose_name="性别")
    mobile = models.CharField(max_length=11, blank=True, null=True)
    user_name = models.CharField(max_length=10)
    avatar = models.CharField(max_length=128, blank=True, null=True)
    bg = models.CharField(max_length=128, blank=True, null=True)
    create_time = models.DateTimeField(default=timezone.now(),db_column='create_ time', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    update_time = models.DateTimeField(default=timezone.now(),blank=True, null=True)
    role = models.ForeignKey(Role, on_delete=models.CASCADE,verbose_name='角色')

    USERNAME_FIELD = 'account'
    objects = UserManager()

    class Meta:
        db_table = 'user'
        verbose_name = '用户'  # 在admin站点中显示的名称
        verbose_name_plural = verbose_name  # 显示的复数名称

    def __str__(self):
        return  self.user_name