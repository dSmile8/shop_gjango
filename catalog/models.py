from django.db import models

from users.models import User

NULLABLE = {'null': True, 'blank': True}


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Категория')
    description = models.TextField(verbose_name='Описание')

    class Meta:
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='модель')
    description = models.TextField(verbose_name='описание')
    image = models.ImageField(upload_to='image/', verbose_name='изображение', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, verbose_name='категория',
                                 related_name='products', **NULLABLE)
    price = models.IntegerField(verbose_name='цена')
    created_at = models.DateField(verbose_name='дата создания')
    updated_at = models.DateField(verbose_name='дата опубликования')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name="Создан пользователем", **NULLABLE)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ('name', 'category', 'price', 'description',)

    def __str__(self):
        return f'{self.name} {self.category} {self.price}'


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='продукт')
    version_number = models.FloatField(verbose_name='номер версии', default=1)
    version_name = models.CharField(max_length=100, verbose_name='название версии', default=None)
    is_current = models.BooleanField(verbose_name='текущая версия', default=False)

    class Meta:
        verbose_name = 'Версию'
        verbose_name_plural = 'Версии'

    def __str__(self):
        return f'{self.version_number}'
