# -*- coding: utf-8 -*-
# czat/models.py

from django.db import models
from django.contrib.auth.models import User


class Wiadomosc(models.Model):

    """Klasa reprezentująca wiadomość w systemie"""
    tekst = models.CharField('treść wiadomości', max_length=250)
    data_pub = models.DateTimeField('data publikacji')
    autor = models.ForeignKey(User)

    class Meta:  # ustawienia dodatkowe
        verbose_name = u'wiadomość'  # nazwa obiektu w języku polskim
        verbose_name_plural = u'wiadomości'  # nazwa obiektów w l.m.
        ordering = ['data_pub']  # domyślne porządkowanie danych

    def __str__(self):
        return self.tekst  # "autoprezentacja"

class Nieobecnosc(models.Model):
    
    """Klasa reprezentująca nieobecność pracownika w systemie"""
    tekst = models.CharField('powod nieobecnosci',max_length=100)
    data_pub = models.DateTimeField('data zgłoszenia')
    data_start = models.DateTimeField('data pierwszego dnia nieobecnosci')
    data_koniec = models.DateTimeField('data ostatniego dnia nieobecnosci')
    autor = models.ForeignKey(User)

    class Meta:
        verbose_name = u'nieobecność'  # nazwa obiektu w języku polskim
        verbose_name_plural = u'nieobecności'  # nazwa obiektów w l.m.
        ordering = ['data_pub']  # domyślne porządkowanie danych

    def __str__(self):
        return self.tekst  # "autoprezentacja"