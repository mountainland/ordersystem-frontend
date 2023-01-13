from django.views.generic import DetailView, ListView, UpdateView, CreateView, TemplateView
from .models import Product, Order, Payment_method, City
from .forms import OrderForm
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.admin.views.decorators import staff_member_required
from django.template.defaulttags import register
from django.http import HttpResponse
from django.conf import settings
from .products import product

import requests

PRODUCT_COUNT = 0

BACKEND_URL = getattr(settings, "BACKEND_URL", None)

# pylint: disable=no-member

PRODUCTS_URL = BACKEND_URL + "/ordersystem/api/products/"
PRODUCTS_URL = PRODUCTS_URL


ORDER_URL = BACKEND_URL + "/ordersystem/api"


# @method_decorator(login_required, name='dispatch')
def get_data():
    product_list = []
    response = requests.get(PRODUCTS_URL)
    count = 0
    for response in response.json():
        product_list.append(product(response))
        count += 1
    return count, product_list


class ProductListView(ListView):
    model = Product

    def get(self, *args, **kwargs):
        product_list = []
        count, product_list = get_data()
        PRODUCT_COUNT = count
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
        response = requests.get(PRODUCTS_URL)
        for response in response.json():
            context[f'product_{count}'] = product(response)
            count += 1

        context['Payment_method'] = Payment_method.objects.all()
        context["City"] = City.objects.all()
        context["show_cities"] = getattr(settings, "SHOW_CITYS", False)
        return context

    def form_valid(self, form):
        print(form.is_valid())

        data = {"order": {}, "ready": False}
        order = data["order"]
        count, product_list = get_data()
        for i in range(1, count):
            order[f"{product_list[i].name}"] = f"{form[f'count_{i}'].value()}"
        answer = requests.post(ORDER_URL, json=data)
        print(answer.text)
        print("Sent")
        return super(OrderCreateView, self).form_valid(form)


@method_decorator(login_required, name='dispatch')
class OrderDetailView(DetailView):
    model = Order


def order_conform(self):
    return render(self, 'Product/thanks.html')
