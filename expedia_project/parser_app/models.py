from django.db import models

# Create your models here.


class AviaTicketsInfo(models.Model):

    search_date = models.DateTimeField(auto_now_add=True)
    flying_from = models.CharField(max_length=255)
    flying_to = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    time = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f'{self.flying_from}-{self.flying_to}'

    class Meta:
        verbose_name = 'Ticket Info'
        verbose_name_plural = 'Avia tickets info'


class FlyingFrom(models.Model):
    name = models.CharField(max_length=255)
    status = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Airport'
        verbose_name_plural = 'Flying From'



class FlyingTo(models.Model):
    name = models.CharField(max_length=255)
    status = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Airport'
        verbose_name_plural = 'Flying To'


