from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=128)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return '{name} ({price})'.format(name=self.name, price=self.price)

    def to_dict(self):
        return {
            'name': self.name,
            'price': '{:2f}'.format(self.price)
            # TODO: Add URL
        }
