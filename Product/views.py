from django.views.generic import ListView, CreateView
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.conf import settings
from Product.products import product


import django


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
        print(response)
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
    template_name = 'Product/order_form.html'

    def get_context_data(self, object_list=None, **kwargs):
        context = dict()
        count = 1
        response = requests.get(PRODUCTS_URL)
        for response in response.json():
            context[f'product_{count}'] = product(response)
            count += 1

        return context

    def post(self, request):
        my_data = request.POST
        data = {"order": {}, "ready": False}
        order = data["order"]
        count, product_list = get_data()
        for i in range(0, count+1):
            try:
                print(i)
                print(product_list[i].name, my_data[f'count_{i}'])
                order[product_list[i].name] = my_data[f'count_{i}']
            except IndexError:
                continue
            except django.utils.datastructures.MultiValueDictKeyError:
                continue

        requests.post(ORDER_URL, json=data)
        context = {}
        return super(CreateView, self).render_to_response(context)


def order_conform(self):
    return render(self, 'Product/thanks.html')
