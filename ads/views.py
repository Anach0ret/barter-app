from django.shortcuts import render
from django.views.generic import DetailView, CreateView
from django_filters.views import FilterView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.utils.http import urlencode
from django.shortcuts import get_object_or_404, redirect

from django.contrib import messages

from . import models, forms, filters



class AdsView(FilterView):
    model = models.Ad
    template_name = "ads/ads_page.html"
    context_object_name = "ads"
    extra_context = {'categories': models.Ad.Category.choices, 'conditions': models.Ad.Condition.choices}
    filterset_class = filters.AdFilter

    paginate_by = 10


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["current_filters"] = urlencode(self.request.GET.dict(), doseq=True)

        return context



class AdDetailView(DetailView):
    model = models.Ad
    template_name = "ads/ad_detail_page.html"
    context_object_name = "ad"
    slug_field = "slug"
    slug_url_kwarg = "slug"



class BarterRequestView(LoginRequiredMixin, CreateView):
    model = models.BarterRequest
    form_class = forms.BarterRequestForm
    template_name = "ads/barter_request_page.html"
    slug_field = "slug"
    slug_url_kwarg = "slug"

    def dispatch(self, request, *args, **kwargs):
        self.receiver_ad = get_object_or_404(models.Ad, slug=kwargs["slug"])
        return super().dispatch(request, *args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["receiver_ad"] = self.receiver_ad
        return context

    def form_valid(self, form):
        barter = form.save(commit=False)
        barter.ad_receiver = self.receiver_ad

        if barter.ad_sender.user == self.receiver_ad.user:
            form.add_error("ad_sender", "You cannot send a barter to your own ad.")
            return self.form_invalid(form)

        barter.save()
        messages.success(self.request, "Barter request sent.")
        return redirect(self.receiver_ad.get_absolute_url())

