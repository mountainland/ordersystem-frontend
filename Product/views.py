from django.views.generic import DetailView, ListView, UpdateView, CreateView, TemplateView
from .models import Product, Order
from .forms import OrderForm
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.admin.views.decorators import staff_member_required



@method_decorator(login_required, name='dispatch')
class ProductListView(ListView):
    model = Product

@method_decorator(login_required, name='dispatch')
class ProductDetailView(DetailView):
    model = Product


@method_decorator(login_required, name='dispatch')
class OrderListView(ListView):
    model = Order

    def get_queryset(self):
        return Order.objects.all().filter(order_by=self.request.user)

@method_decorator(staff_member_required, name='dispatch')
class OrderAdminView(ListView):
    model = Order

    def get_queryset(self):
        return Order.objects.all().filter(delivered=False)



@method_decorator(login_required, name='dispatch')
class OrderCreateView(CreateView):
    model = Order
    form_class = OrderForm
    success_url = '/order/conformed/'

    def get_context_data(self,  object_list=None, **kwargs):
        context = super(OrderCreateView, self).get_context_data(**kwargs)
        context['product_1'] = get_object_or_404(Product, slug="mokkapala")
        context['product_2'] = get_object_or_404(Product, slug="pipari")
        context['product_3'] = get_object_or_404(Product, slug="feta")
        return context


    def form_valid(self, form):
        product_1 = Product.objects.get(slug__iexact='mokkapala')
        product_2 = Product.objects.get(slug__iexact='pipari')
        product_3 = Product.objects.get(slug__iexact='feta')
        form.instance.product_1 = product_1
        form.instance.product_2 = product_2
        form.instance.product_3 = product_3
        form.instance.cost = ((int(form.instance.count_1) * int(product_1.price)) + (int(form.instance.count_2) * int(product_2.price)) + (int(form.instance.count_3) * int(product_3.price)))
        return super(OrderCreateView, self).form_valid(form)

@method_decorator(login_required, name='dispatch')
class OrderDetailView(DetailView):
    model = Order


def order_conform(self):
    return render(self, 'Product/thanks.html')

