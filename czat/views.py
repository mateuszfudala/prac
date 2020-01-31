# -*- coding: utf-8 -*-
# czat/views.py

from django.shortcuts import render
# from django.http import HttpResponse
from django.views.generic.edit import CreateView
from czat.models import Wiadomosc, Nieobecnosc
from django.utils import timezone
from django.contrib import messages
from django.views.generic.edit import UpdateView

def index(request):
    """Strona główna aplikacji."""
    # return HttpResponse("Witaj w aplikacji Czat!")
    return render(request, 'czat/index.html')

class DodajWiadomosc(CreateView):
    model = Wiadomosc
    fields = ['tekst', 'data_pub']
    context_object_name = 'wiadomosci'
    success_url = '/wiadomosci'

    def get_initial(self):
        initial = super(DodajWiadomosc, self).get_initial()
        initial['data_pub'] = timezone.now()
        return initial

    def get_context_data(self, **kwargs):
        context = super(DodajWiadomosc, self).get_context_data(**kwargs)
        context['wiadomosci'] = Wiadomosc.objects.all()
        return context

    def form_valid(self, form):
        wiadomosc = form.save(commit=False)
        wiadomosc.autor = self.request.user
        wiadomosc.save()
        messages.success(self.request, "Dodano wiadomość!")
        return super(DodajWiadomosc, self).form_valid(form)

class EdytujWiadomosc(UpdateView):
    model = Wiadomosc
    from czat.forms import EdytujWiadomoscForm
    form_class = EdytujWiadomoscForm
    context_object_name = 'wiadomosci'
    template_name = 'czat/wiadomosc_form.html'
    success_url = '/wiadomosci'

    def get_context_data(self, **kwargs):
        context = super(EdytujWiadomosc, self).get_context_data(**kwargs)
        context['wiadomosci'] = Wiadomosc.objects.filter(
            autor=self.request.user)
        return context

    def get_object(self, queryset=None):
        wiadomosc = Wiadomosc.objects.get(id=self.kwargs['pk'])
        return wiadomosc

class DodajNieobscnosc(CreateView):
    model = Nieobecnosc
    fields = ['tekst','data_pub','data_start','data_koniec']
    context_object_name = 'nieobecnosci'
    success_url = '/nieobecnosci'

    def get_initial(self):
        initial = super(DodajNieobscnosc, self).get_initial()
        initial['data_pub'] = timezone.now()
        return initial

    def get_context_data(self, **kwargs):
        context = super(DodajNieobscnosc, self).get_context_data(**kwargs)
        context['nieobecnosci'] = Nieobecnosc.objects.all()
        return context

    def form_valid(self, form):
        nieobecnosc = form.save(commit=False)
        nieobecnosc.autor = self.request.user
        nieobecnosc.save()
        messages.success(self.request, "Zgłoszono nieobecnosc!")
        return super(DodajNieobscnosc, self).form_valid(form)

class EdytujNieobecnosc(UpdateView):
    model = Nieobecnosc
    from czat.forms import EdytujNieobecnoscForm
    form_class = EdytujNieobecnoscForm
    context_object_name = 'nieobecnosci'
    template_name = 'czat/nieobecnosc_form.html'
    success_url = '/nieobecnosci'

    def get_context_data(self, **kwargs):
        context = super(EdytujNieobecnosc, self).get_context_data(**kwargs)
        context['nieobecnosci'] = Nieobecnosc.objects.filter(
            autor=self.request.user)
        return context

    def get_object(self, queryset=None):
        nieobecnosc = Nieobecnosc.objects.get(id=self.kwargs['pk'])
        return nieobecnosc