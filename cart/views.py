from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.base import TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from accounts.models import Profile
from productos.models import Producto
from .models import Order, OrderItem, Coupon, Wish
from .forms import OrderForm
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from datetime import datetime
from django.core.paginator import Paginator
from django.urls import reverse, reverse_lazy
from datetime import date


@login_required()
def add_to_cart(request, *args, **kwargs):

    if request.method == 'GET':
        user_profile = Profile.objects.get(user=request.user)

        producto_id = request.GET.get('item_id', '')  
        cantidad = request.GET.get('cantidad', '')
        talle = request.GET.get('talle', '') 
        modelo = request.GET.get('modelo', '')
        path_redirect = request.GET.get('path_redirect', '')

        if producto_id == '' or producto_id == None:
            return redirect(reverse('my_cart'))
        else:
            producto = Producto.objects.get(id=producto_id)

        print('GET: {} {} {} {}'.format(producto_id, cantidad, talle, modelo))

        if producto.estado and cantidad != '' and talle != '' and modelo != '':
    
            user_order, status = Order.objects.get_or_create(owner=user_profile, is_ordered=False)
            code = user_order.id
            if status:
                user_order.ref_code += code
                user_order.save()
    
            order_item, status = OrderItem.objects.get_or_create(producto = producto, size = talle, model = modelo, owner = user_profile, is_ordered=False)
            if status:
                order_item.quantity = cantidad
            else:
                order_item.quantity = order_item.quantity + int(cantidad)
            order_item.save()
    
            if not order_item in user_order.items.all():
                user_order.items.add(order_item)
                print("Agregado al carrito")

            if path_redirect == '':
                return redirect(reverse('my_cart'))
            else:
                return HttpResponseRedirect(path_redirect)
        else:
            return redirect(reverse('my_cart'))
    # show confirmation message and redirect back to the same page
    return redirect(reverse('my_cart'))
    
@login_required()
def delete_from_cart(request):

    if request.method == 'GET':

        orderitem_id = request.GET.get('orderitem_id', '')
        path_redirect = request.GET.get('path_redirect', '')
        if orderitem_id != '':
            item_to_delete = OrderItem.objects.filter(id=orderitem_id)
            if item_to_delete.exists():
                item_to_delete[0].delete()
                messages.info(request, "Item has been deleted")
        
        if path_redirect != '':
            return HttpResponseRedirect(path_redirect)
        else: 
            return redirect(reverse('my_cart'))
        

    return redirect(reverse('my_cart'))

@login_required()
def add_wishlist(request):

    if request.method == 'GET':
        user_profile = Profile.objects.get(user=request.user)

        producto_id = request.GET.get('orderitem_id', '')
        path_redirect = request.GET.get('path_redirect', '')

        if producto_id == '' or producto_id == None:
            return redirect(reverse('wish_list'))
        else:
            producto = Producto.objects.get(id=producto_id)

        wish, status = Wish.objects.get_or_create(owner = user_profile, producto = producto)
        
        if status:
            wish.save()
        
        if path_redirect != '':
            return HttpResponseRedirect(path_redirect)
        else: 
            return redirect(reverse('wish_list'))
        

    return redirect(reverse('wish_list'))
    
@login_required()
def my_cart(request):
    coupon = None
    
    if request.method == 'POST':
        code  = request.POST.get('coupon')
        if not code == '' or None:
            try:
                coupon = Coupon.objects.get(code = code, estado = True)
            except Exception:
                coupon = None
            

    #user_profile = Profile.objects.get(user=request.user)
    #user_order, status = Order.objects.get_or_create(owner=user_profile, is_ordered=False)
    #context={"profile":user_profile, "order":user_order, "coupon": coupon}
    context={"coupon": coupon}
    
    return render(request,'cart/my_cart.html', context)
    
@login_required()
def finish_order(request):
    
    if request.method == 'POST':
        coupon_id = int(request.POST.get('coupon_id'))
        order_id = request.POST.get('order_id')
        
        order = Order.objects.get(id = order_id)
        order.is_ordered = True
        
        subtotal = order.get_cart_total()
        
        if coupon_id > 0:
            coupon = Coupon.objects.get(id = coupon_id)
            discount_1 = coupon.amount
            discount_2 = (subtotal*coupon.percentage)/100
            total = subtotal - discount_1 - discount_2
        else:
            total = subtotal
            
        order.total = total
        
        order_items = order.items.all()

        order_items.update(is_ordered=True, date_ordered=datetime.now())
        
        
        order.save()
        print("terminado")

        texto= "Tengo un pedido en espera, Pedido Nº: {}, link: https://localhost.com/cart/my-orders/{}/".format(order_id, order_id)
        cadena = "https://api.whatsapp.com/send?phone=595993326313&text={}".format(texto)
        return redirect(cadena)
        
    return redirect(reverse('my_orders')+"?chout=ok")

@method_decorator(login_required, name='dispatch')
class OrderListView(ListView):
    model = Order
    paginate_by = 10
    
    def get_queryset(self, *args, **kwargs):
        profile = Profile.objects.get(user = self.request.user)
        qs = Order.objects.filter(is_ordered = True, owner = profile).order_by('-date_ordered')
        
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

@method_decorator(login_required, name='dispatch')
class WishListView(ListView):
    model = Wish
    paginate_by = 10
    template_name = "cart/wish_list.html"

    def get_queryset(self, *args, **kwargs):
        profile = Profile.objects.get(user = self.request.user)
        qs = Wish.objects.filter(owner = profile).order_by('-date_created')
        return qs
        
class OrderView(TemplateView):
    model = Order
    template_name = "cart/order_detail.html"
    
    def get_context_data(self, **kwargs):
        context = super(OrderView, self).get_context_data(**kwargs)
        order = Order.objects.get(id = self.kwargs['pk'])
        context['items'] = order.items.all()
        context['profile_order'] = Profile.objects.get(id = order.owner.id)
        return context


@login_required()
def order_detail(request, id):

    user_order = Order.objects.get(id = id)
    items = user_order.items.all()
    
    profile = Profile.objects.get(id = user_order.owner.id)

    user_user = profile.user
    my_orders = {}
    context={"user_order":user_order, "items":items, "user_user":user_user, "my_orders":my_orders}
    print(context)
    
    return render(request,'cart/order_detail.html', context)

@method_decorator(staff_member_required, name='dispatch')
class OrderAdminUpdate(UpdateView):
    model = Order
    form_class = OrderForm
    template_name = "cart/admin_order_detail.html"
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('admin_order_list')
    
    def get_context_data(self, **kwargs):
        context = super(OrderAdminUpdate, self).get_context_data(**kwargs)
        order = Order.objects.get(id = self.kwargs['pk'])
        context['items'] = order.items.all()
        context['profile_order'] = Profile.objects.get(id = order.owner.id)
        return context

@method_decorator(staff_member_required, name='dispatch')
class OrderAdminList(ListView):
    model = Order
    template_name = "cart/admin_order_list.html"

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




    
