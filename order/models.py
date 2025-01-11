from django.db import models
from userApp.models import User
# Create your models here.


class Order(models.Model):
    description = models.CharField(max_length=100, null=False, blank=False)
    user = models.ForeignKey(User, to_field='name', on_delete=models.CASCADE)
    productId = models.CharField(max_length=20)
    orderid = models.CharField(max_length=20)

    def __str__(self):
        self.user

    def to_dict(self):
        return {
            "orderid": self.orderid,
            "user": self.user.to_dict(),
            "productId": self.productId,
            "description": self.description
        }
