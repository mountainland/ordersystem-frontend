from django.views.generic import ListView, CreateView
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.conf import settings
from Product.products import product

import requests
# pylint: disable=no-member, invalid-name

PRODUCT_COUNT = 0

BACKEND_URL = getattr(settings, "BACKEND_URL", None)


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
    def get(self, *args, **kwargs):
        product_list = []
        count, product_list = get_data()
        PRODUCT_COUNT = count
        context = {'object_list': product_list}
        return render(self.request, 'product_list.html', context=context)


@method_decorator(login_required, name='dispatch')
class OrderCreateView(CreateView):
    success_url = '/order/conformed/'

    def get_context_data(self, object_list=None, **kwargs):
        context = super(OrderCreateView, self).get_context_data(**kwargs)
        count = 1
        response = requests.get(PRODUCTS_URL)
        for response in response.json():
            context[f'product_{count}'] = product(response)
            count += 1

        return context

    def form_valid(self, form):
        print(form.is_valid())

        data = {"order": {}, "ready": False}
        order = data["order"]
        count, product_list = get_data()
        for i in range(1, count):
            order[f"{product_list[i].name}"] = f"{form[f'count_{i}'].value()}"
        requests.post(ORDER_URL, json=data)
        return super(OrderCreateView, self).form_valid(form)


def order_conform(self):
    return render(self, 'Product/thanks.html')
