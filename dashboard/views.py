from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import FormView, ListView, UpdateView, DeleteView, TemplateView
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from rest_framework.authtoken.models import Token

from django.contrib import messages

from . import forms
from ads import models




class MyAdsView(LoginRequiredMixin, ListView):
    model = models.Ad
    template_name = "dashboard/my_ads_block.html"
    context_object_name = "user_ads"
    paginate_by = 10

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user).order_by("-created_at")



class AdUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = models.Ad
    form_class = forms.AdForm
    template_name = "dashboard/ad_form.html"
    success_url = reverse_lazy("dashboard")
    extra_context = {'title': 'Edit Ad', 'button_title': 'Edit'}

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "Ad updated successfully.")
        return super().form_valid(form)

    def test_func(self):
        return self.get_object().user == self.request.user


class AdCreateView(LoginRequiredMixin, FormView):
    template_name = "dashboard/ad_form.html"
    form_class = forms.AdForm
    success_url = reverse_lazy("dashboard")
    extra_context = {'title': 'Create Ad', 'button_title': 'Create'}

    def form_valid(self, form):
        ad = form.save(commit=False)
        ad.user = self.request.user
        ad.save()
        messages.success(self.request, "Ad created successfully.")
        return super().form_valid(form)


class AdDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = models.Ad
    template_name = "dashboard/delete_ad.html"
    success_url = reverse_lazy("dashboard")

    def post(self, request, *args, **kwargs):
        messages.success(request, "Ad deleted successfully.")
        return super().post(request, *args, **kwargs)

    def test_func(self):
        return self.get_object().user == self.request.user


class BartersBoxListView(LoginRequiredMixin, TemplateView):
    template_name = "dashboard/barters_box.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user

        context["sent_barters"] = models.BarterRequest.objects.filter(ad_sender__user=user).select_related("ad_receiver")
        context["received_barters"] = models.BarterRequest.objects.filter(ad_receiver__user=user).select_related("ad_sender")

        return context


class BarterStatusUpdateView(LoginRequiredMixin, View):
    def post(self, request, pk):
        barter = get_object_or_404(models.BarterRequest, pk=pk, ad_receiver__user=request.user)
        status = request.POST.get("status")

        if barter.status != models.BarterRequest.Status.PENDING:
            messages.info(request, "This request has already been processed.")
        elif status in (models.BarterRequest.Status.ACCEPTED, models.BarterRequest.Status.DECLINED):
            barter.status = status
            barter.save()
            messages.success(request, f"Request {status}.")
        else:
            messages.error(request, "Invalid status value.")

        return redirect("barters_box")


@login_required
def token_view(request):
    token, _ = Token.objects.get_or_create(user=request.user)

    return render(request, 'dashboard/token_block.html', {
        'token': token.key,
    })