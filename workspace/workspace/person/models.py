import re
from django.contrib.auth.models import (AbstractBaseUser, PermissionsMixin, UserManager)
from django.db import models
from django.core import validators

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField('username', max_length=30, unique=True, validators=[validators.RegexValidator(re.compile('^[\w.@+-]+$'),
            'O nome de usuário só pode conter letras, digitos ou os '
            'seguintes caracteres: @/./+/-/_', 'invalid')])
    email = models.EmailField('E-mail', unique=True)
    name = models.CharField('Nome', max_length=100)
    image = models.ImageField('Imagem de Perfil', upload_to='media/person/img', default='media/person/img/noavatar.png')
    is_active = models.BooleanField('Esta Ativo?', blank=True, default=True)
    is_superuser = models.BooleanField('Admin', blank=True, default=False)
    is_staff = models.BooleanField('É da equipe?', blank=True, default=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.name or self.username
    def get_short_name(self):
        return self.username
    def get_full_name(self):
        return str(self)
    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = "Usuários"