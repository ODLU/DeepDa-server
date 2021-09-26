from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)


class UserManager(BaseUserManager):
    def create_user(self, userid, nickname, email=None, password=None):
        if not userid:
            raise ValueError('Users must have an id')

        user = self.model(
            userid=userid,
            nickname=nickname,
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, userid, nickname, password):
        user = self.create_user(
            userid,
            nickname=nickname,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    userid = models.CharField(
        max_length=255,
        unique=True,
        default="user"
    )
    nickname = models.CharField(max_length=30, default="user")
    email = models.EmailField(verbose_name='email', null=True)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'userid'
    REQUIRED_FIELDS = ['nickname']

    def __str__(self):
        return self.userid

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
