from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.core.mail import send_mail


from .models import *
from .forms import AdsForm



class AdsList(ListView):
    model = Ads
    ordering = 'name'
    template_name = 'Ads_list.html'
    context_object_name = 'Ads'



class Ads(DetailView):
    model = Ads
    template_name = 'Ads.html'
    context_object_name = 'Ads'

@login_required
class AdsCreate(PermissionRequiredMixin, CreateView):
    permission_required = ('BulletinBoard.ads_create',)
    form_class = AdsForm
    model = Ads
    template_name = 'ads_create.html'

    def form_valid(self, form):
        form.save(commit=False)
        return super().form_valid(form)

@login_required
class AdsUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = ('BulletinBoard.ads_update',)
    form_class = AdsForm
    model = Ads
    template_name = 'ads_update.html'

@login_required
class MyAdsList(ListView, User):
    if Ads.Ads_author == User:
        model = Ads
        ordering = 'name'
        template_name = 'MyAds.html'
        context_object_name = 'MyAds'



