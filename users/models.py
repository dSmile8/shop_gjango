from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'null': True, 'blank': True}


class User(AbstractUser):
    '''Users model'''
    username = None
    email = models.EmailField(unique=True, verbose_name='Email')
    phone = models.CharField(max_length=15, verbose_name='Телефон', help_text='Введите номер телефона', **NULLABLE)
    country = models.CharField(max_length=100, verbose_name='Страна', help_text='Введите вашу страну', **NULLABLE)
    avatar = models.ImageField(upload_to='users/avatars/', verbose_name='аватар', help_text='Выберете файл', **NULLABLE)
    token = models.CharField(max_length=100, verbose_name='Токен', **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email
