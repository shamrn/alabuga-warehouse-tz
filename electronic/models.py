from django.db import models
from django.core.validators import MinValueValidator
from datetime import datetime
import random
import string


class Category(models.Model):
    """
    Модель категорий
    """
    name = models.CharField('Название категории', max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Manufacturer(models.Model):
    """
    Модель производителя
    """
    name = models.CharField('Название производителя', max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Производитель'
        verbose_name_plural = 'Производители'


class Product(models.Model):
    """
    Модель товара
    """
    code = models.CharField('Код товара', max_length=8, unique=True,
                            default=''.join(random.choice(string.ascii_letters + string.digits) for _ in range(8)),
                            help_text='Код генерируется автоматически, к изменению недоступен')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, verbose_name='Производитель')
    name = models.CharField('Название товара', max_length=200)
    price = models.DecimalField('Стоимость', max_digits=19, decimal_places=2, validators=[MinValueValidator(0.0)])
    quantity = models.IntegerField('Колличество товара', default=0)
    update_date = models.DateField(auto_now=True)

    def __init__(self, *args, **kwargs):
        """
        При инициализации объекта, сохраняем старое значение колличества товара
        """
        super().__init__(*args, **kwargs)
        self.old_quantity = self.quantity

    def save(self, *args, **kwargs):
        """
        Проверяем старое кол-во товара, если товар изменился, меняем дату на актуальную
        """
        if self.old_quantity != self.quantity:
            self.update_date = datetime.now()
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
