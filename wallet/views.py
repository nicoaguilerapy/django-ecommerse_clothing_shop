from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from accounts.models import Profile
from cart.models import Order
from .models import *

@method_decorator(login_required, name='dispatch')
class MyWalletView(TemplateView):
    template_name = 'wallet/my_wallet.html'

    def get_context_data(self, **kwargs):
        context = super(MyWalletView, self).get_context_data(**kwargs)
        profile = Profile.objects.get(user = self.request.user)
        orders = Order.objects.filter(is_ordered = True, owner = profile).order_by('-date_ordered')
        wallet = Wallet.objects.get(owner = profile)

        context['profile'] = profile
        context['orders'] = orders
        context['wallet'] = wallet

        return context

@method_decorator(login_required, name='dispatch')
class OrderView(TemplateView):
    template_name = 'wallet/order.html'

    def get_context_data(self, **kwargs):
        context = super(OrderView, self).get_context_data(**kwargs)
        profile = Profile.objects.get(user = self.request.user)
        transacciones = Transaction.objects.filter(owner = profile)
        wallet = Wallet.objects.get(owner = profile)

        context['profile'] = profile
        context['transacciones'] = transacciones
        context['wallet'] = wallet
        return context

@method_decorator(login_required, name='dispatch')
class HistoryView(TemplateView):
    template_name = 'wallet/transaction_history.html'

    def get_context_data(self, **kwargs):
        context = super(HistoryView, self).get_context_data(**kwargs)
        profile = Profile.objects.get(user = self.request.user)
        transacciones = Transaction.objects.filter(owner = profile)
        wallet = Wallet.objects.get(owner = profile)

        context['profile'] = profile
        context['transacciones'] = transacciones
        context['wallet'] = wallet
        return context
