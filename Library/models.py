from django.db import models

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=32)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    pub_date = models.DateField()
    publish = models.ForeignKey(
        to="Publish", to_field="id", on_delete=models.CASCADE)
    authors = models.ManyToManyField(to="Author")


class Publish(models.Model):
    name = models.CharField(max_length=32)
    city = models.CharField(max_length=32)
    email = models.EmailField()


class Author(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField()
    email = models.EmailField()
    au_detail = models.OneToOneField(
        to="AuthorDetail", to_field="id", on_delete=models.CASCADE)


class AuthorDetail(models.Model):
    gender_choices = (
        (0, '女'),
        (1, '男'),
        (2, '保密'),
    )
    gender = models.SmallIntegerField(choices=gender_choices)
    tel = models.CharField(max_length=32)
    address = models.CharField(max_length=64)
    birthday = models.DateField()
