from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.utils.text import slugify


class Tag(models.Model):
    '''
    Tag model.
    '''
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    parrent = models.ForeignKey('self',models.SET_NULL,null=True,blank=True,related_name='childs')
    level = models.PositiveIntegerField()

    def save(self, *args, **kwargs):
        if(self.parrent == self):
            self.parrent = None
        parrent = self.parrent
        self.level = parrent.level + 1 if parrent else 0
        self.slug = slugify(self.name, True)
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.slug


class CustomUser(AbstractUser):
    '''
    Custom user model
    '''
    is_company_admin = models.BooleanField(default=False)
    tags = models.ManyToManyField('Tag', blank=True)

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
