from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


class Car(models.Model):

    # Опис моделі в базі данних SQL
    vin = models.CharField(verbose_name='Vin', unique=True, db_index=True, max_length=50)
    color = models.CharField(verbose_name='Color', max_length=50)
    brand = models.CharField(verbose_name='Brand', max_length=50)
    CAR_TYPES = (
        (1, 'Monday'),
        (2, 'Tuesday'),
        (3, 'Wednesday'),
        (4, 'Thursday'),
        (5, 'Friday'),
        (6, 'Saturday'),
        (7, 'Sunday'),
    )
    car_type = models.IntegerField(verbose_name='Car_Type', choices=CAR_TYPES)
    user = models.ForeignKey(User, verbose_name='User', on_delete=models.CASCADE)
