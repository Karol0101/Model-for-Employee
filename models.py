from django.db import models
from django.utils import timezone
import re
from django.core.validators import EmailValidator, MinLengthValidator, MaxLengthValidator


# class shoes_details:
#   shoes_brand = models.TextField(max_length=50)
#  shoes_size = models.IntegerField(primary_key=True)
# shoes_color = models.TextField(max_length=50)
#shoes_type = models.TextField(max_length=50)


class customer:
    cust_name = models.TextField(max_length=50)
    cust_address = models.TextField(max_length=50)
    cust_number = models.IntegerField(max_length=50)
    email = models.EmailField(max_length=50, validators=[EmailValidator(
    ), MinLengthValidator(7), MaxLengthValidator(100)])
    order_time = models.DateTimeField(default=timezone.now, null=False)


class Meta:
    db_table = 'customer'
    ordering = ['order_time']
