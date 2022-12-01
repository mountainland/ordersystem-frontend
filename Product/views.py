from django.views.generic import DetailView, ListView, UpdateView, CreateView, TemplateView
from .models import Product, Order, Payment_method, City
from .forms import OrderForm
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.admin.views.decorators import staff_member_required
from django.template.defaulttags import register
from django.http import HttpResponse

# pylint: disable=no-member
PRODS = []


#@method_decorator(login_required, name='dispatch')
class ProductListView(ListView):
    model = Product

    def get(self, *args, **kwargs):
        product_list = Product.objects.all()
        context = {'object_list': product_list}
        return render(self.request, 'product_list.html', context=context)

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
    
    def get_context_data(self, object_list=None, **kwargs):
        context = super(OrderCreateView, self).get_context_data(**kwargs)
        count = 1
        for product in Product.objects.all():
            context[f'product_{count}'] = product
            PRODS.append(str(product))
            count += 1
        context['Payment_method'] = Payment_method.objects.all()
        context["City"] = City.objects.all()
        return context


    def form_valid(self, form):
        print(form.is_valid())
        product_1 = Product.objects.get(slug__iexact=PRODS[0])
        product_2 = Product.objects.get(slug__iexact=PRODS[1])
        product_3 = Product.objects.get(slug__iexact=PRODS[2])
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

