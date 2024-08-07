from django.shortcuts import render, HttpResponse
from productos.models import *
from social.models import *
from blog.models import *
from cart.models import *
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView
from django.views.generic.edit import UpdateView
from django.views.generic.detail import DetailView

from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect
from django.shortcuts  import get_object_or_404
from django.db.models import Q
from productos.forms import *
from social.forms import *
from pages.forms import *
from blog.forms import *
from cart.forms import *
from datetime import date

class StaffRequired(object):
    
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super(StaffRequired, self).dispatch(request, *args, **kwargs)



class Index(TemplateView):
	template_name = 'core/index.html'

	def get_context_data(self, **kwargs):
		context = super(Index, self).get_context_data(**kwargs)
		cover_pages = CoverPage.objects.filter(visibility = True)
		posts = Post.objects.filter(status = True)
		context['cover_pages'] = cover_pages
		context['posts'] = posts
		return context


@method_decorator(staff_member_required, name='dispatch')
class OrderAdminList(ListView):
    model = Order
    template_name = "core/admin/cart/order_list.html"

    def get_queryset(self, *args, **kwargs):
        qs = Order.objects.filter(is_ordered = True).order_by('-date_ordered')
        
        if self.request.GET.get('status'):
            qs = qs.filter(status = self.request.GET.get('status')).order_by('-date_ordered')
        
        if self.request.GET.get('date'):
            today = date.today()
            if self.request.GET.get('date') == 'today':
                qs = qs.filter(date_ordered__year = today.year,
                               date_ordered__month = today.month,
                               date_ordered__day = today.day).order_by('-date_ordered')
            else:
                if self.request.GET.get('date') == 'month':
                    qs = qs.filter(date_ordered__year = today.year,
                                   date_ordered__month = today.month).order_by('-date_ordered')
        return qs


