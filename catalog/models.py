from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Категория')
    description = models.TextField(verbose_name='Описание')

    class Meta:
        verbose_name = 'Категория'
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

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ('name', 'category', 'price', 'description',)

    def __str__(self):
        return f'{self.name} {self.category} {self.price}'
