# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


# class Test(models.Model):
#     id = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'test'


class User(models.Model):
    account = models.CharField(max_length=20, blank=True, null=True)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=20, blank=True, null=True)
    gender = models.IntegerField()
    mobile = models.CharField(max_length=11, blank=True, null=True)
    user_name = models.CharField(max_length=10)
    avatar = models.CharField(max_length=128, blank=True, null=True)
    bg = models.CharField(max_length=128, blank=True, null=True)
    create_time = models.DateTimeField(db_column='create_ time', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    update_time = models.DateTimeField(blank=True, null=True)
    role_id = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'user'
        verbose_name = '用户'  # 在admin站点中显示的名称
        verbose_name_plural = verbose_name  # 显示的复数名称
