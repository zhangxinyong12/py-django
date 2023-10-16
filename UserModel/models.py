from django.db import models

# Create your models here.
# 数据库模型


class User(models.Model):
    GENDER_CHOICES = (
        (1, '男'),
        (2, '女')
    )

    name = models.CharField(max_length=20)
    age = models.IntegerField()
    sex = models.IntegerField(choices=GENDER_CHOICES)
