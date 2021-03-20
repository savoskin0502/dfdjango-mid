from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.conf import settings


class BookJournalBase(models.Model):
    name = models.CharField(max_length=20, blank=True, null=False)
    price = models.FloatField(null=False)
    description = models.TextField(max_length=300, blank=True)
    created_at = models.DateField(default=timezone.now, blank=True, null=False)

    class Meta:
        verbose_name = 'BookJournalBase'
        verbose_name_plural = 'BookJournalsBase'
        abstract = True


class Book(BookJournalBase):
    class Genres(models.TextChoices):
        NOT_DEFINED = 'NotDefined', _('Not Defined')
        HORROR = 'Horror', _('Horror')
        COMEDY = 'Comedy', _('Comedy')
    num_pages = models.IntegerField(default=1)
    genre = models.CharField(max_length=10, choices=Genres.choices,
                             default=Genres.NOT_DEFINED)

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'


class Journal(BookJournalBase):
    class Types(models.TextChoices):
        BULLET = 'Bullet', _('Bullet')
        FOOD = 'Food', _('Food')
        TRAVEL = 'Travel', _('Travel')
        SPORT = 'Sport', _('Sport')

    type = models.CharField(max_length=10, choices=Types.choices,
                            null=False)
    publisher = models.ForeignKey(settings.AUTH_USER_MODEL,
                                  on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Journal'
        verbose_name_plural = 'Journals'
