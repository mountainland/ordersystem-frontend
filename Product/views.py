from django.views.generic import DetailView, ListView, UpdateView, CreateView, TemplateView
from .models import Product, Order, Payment_method, City
from .forms import OrderForm
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.admin.views.decorators import staff_member_required
from django.template.defaulttags import register
from django.http import HttpResponse
from .products import product

import requests
# pylint: disable=no-member
PRODS = []

BACKEND = "https://botsarefuture-solid-happiness-p56jq4j774xh97p5-8000.preview.app.github.dev"

PRODUCTS_URL = BACKEND + "/ordersystem/api/products/"

#@method_decorator(login_required, name='dispatch')
class ProductListView(ListView):
    model = Product

    def get(self, *args, **kwargs):
        product_list = []
        cookies = {"__Host-vso-pf":"A7494ECC62B836A34BCD3165C0B2E935%3AJUks9KNsKkrFPMBqFZL478Biwz6uH78P7UgaUumSoLTz9qZSfT2eQ8yLw9kazx6%2FKSpCPKT2F%2F04p0Jn%2FTQlYwaJAEgCnTOvY9lx8SDsXdGqXJqTrXqjpVwpjw92wEdDw3vzS1fD%2FGEvDIJ%2FRRD%2BmJZcd2KcJV99zP5akrl1750b6xp9L66hUuM%2FPiyHOKB51KhIoATJ4xWtFhUAbU%2BhV41PlPPjTZadZySpzEFCC1bxjD8FL%2FaGmekx%2FJNSoZx9PiZNsrGvFWrCBkXBQrj%2FoYrXM%2FtztXdnVLbBQ45SpP%2BO5C12y223wokzjFOcsHs1slVTODcFAvw3%2FuAr2A2jTwepsyjnlMDD8yMTLGNRoE1pc4ovXp2UMmUFELNYg%2FbQc9r3GI51AeQCPUxSqwpYxp81QP321V0UUgC9bBPVmuUWIOOH5AsX9BhHgA1L7FypUvOXSrpw9KyNW%2FLYGS6PbJ01x%2FeCp17t729Oz4s%2BIDxHDYuqqoIYmWQZAEXP8uICNCuUcND0E4XVAkqJlGsUDKj83b5p%2Bat8r2E5WSjRl0KWKDncNRyJrZnxZzFA1fod4e5VFvZDWrd%2BstRjYH%2BWjVZ1NHAdF5RvJKmtKO2Z7t5iuRNzX82wEDifRuigyTYCHA5PsdDklhWY7gs%2FgfL6qBAWtwwqGYm9o4cmMkXqBKSPZm5Mgail0osjgCTJqWHy6L4LJBhruRPWkk2Z1X%2BNCP7X4%2Bp79JVKmy1VtjIyPxEFmS%2Bd1L04GkWX%2BU4LqGxGE7N%2BMYJIcHOzDNee3jHULmosu3YFONTn2YS%2Fnt%2BIp%2BjaR3X74fGeX3A7p%2BoYSmboI%2Bz7SXfaIqreHHmMlQMiQMZyybBcB0cgGAIfsfcJhP8i%2FLpQTIHlRV7xy6rB5m7FQ%2Bv5UIRFsljMnylTqx236vnOVxlqvVauhBHKvQIlvhZ5XqugwOl2HIbLWhY1gBCXXksqj2lt3GlGD%2FBoB47NUj57Klr63PBPFLLXaSwApbNuSGEwFHvvpqgFZgEjnUjtkmENNqqGnD0jm%2BQlSTTMa6gs%2FRTmywJmnTacM2eYBFkbvK%2BjTxkdaojeFgJKZnBuex0ckrm%2B24u7d9K2Ui5jkQXflNEcyo4ZcHw7flsDOwnyMT5U2rughYThKzM%2FwAYlm1daEh3wRy%2BCqw%2F8PXQhcFYxvHjHuYuSxrV5Mfqv%2BzFZwfUNK0ostbStpcEPkhmo28ut2mfIwTcO55sEdgu4Z9sLNi0%2Bk%2FWr5iJyCC14lzDPgQLjGXoYzZ4pyrQxYCtwfCaxULGN1%2BZnc05TtXrQQPLHp70VTxq4KgkqlrqwpQmsHDUx7HzoglUWQK0zhE8%2BLarfNSpP%2BkqGu9pHXjGXz0vHgWkD%2FHb2QReArXpL7LIDPEtaX2MaIvz3bJn8S1BO6z%2FI8q2qby6NAXWS2lvYOUNOSSfg4zu8Qd%2F162RDjAMhX9XvU6Z%2FBv4b%2FZfB6H2MDCXe4kcwITdiqyYQXWDrOuniDtqd2Teuxndq4q0NYOkPx3DET%2B7mKrdhw54MpmOorKukwK3N74KPGivTxKMrhuyWSNdvGFwMVc9oS%2FBciNzBS535tRMX9EXleKRrRhZ6HkbgrZf%2BB08%2FIX5XM9EE9QhSFqwPhmrsKNnok9R2uluTmqt6WEG4CN1wft0F3ZkZcIzGtKTEgTpi9BVvyaK4S5W8n0Pr4Z49JEJEiLhR2nbp76k3%2F7jK4ggK84bO6JhrnVoeIfR6zaLAuSen66mQN3Bl5Cf5VvmT0ThPy2vmwA%2FbktJHz7UtaFa%2FzUrRm2u2zp2RH%2F6aTtiv1EvtWHtsKESCPwT2uHZsRNybC41ZAQMzKkYfgFREDEy6boRTA5%2B3A%2BG7kvQVtC6wo7244RpasULYD%2FN8IQMsAEZUoa%2FWyj1xbn%2FR%2BNfy9aTqaOHsxkr8zVm4c9HUCzvpqlMQToqFZdOEGjLNL6tIlrtQypAxoiz7srjjEAdPmpq4wjav2dlOhdxoF%2F0%2F4GdQdfEeZHfYMjRhHggLdsFbNvnpA3%2B2Xufqy9mrmtVrshnO7eUAIyqwsfryIZGSd47DH5%2FdrWH%2BOM%2FcdS7tQ8l%2FvchTMxgB95FeoxobVQImrgKKypGonmBpfLa4phPMnAAA9yt5h1o2mJiKTtEjbn3QNJSGEtZQuvVMje6YPrLADGkuObueCB4s6%2Bn%2Bdc0YsWQ8eTGQJNJcIoX9JghZ%2BaJ30%2BIemehLGNr%2FpyqLihrI0%2F%2BxrD091ANsS6EbO3TaGfB0YBIV9XBquUc2lhd5SZBqtZpV1s5R%2Bvcgtgd7UCWSpKtVhqyE3gEHzbaQ6NPP7hIBIUmHdYEGtZJ4ntlHpVX0PppAUT3cAtlqyGkN4rXOJSGnOXRIvLSrT0bgjxhzP583k691yXzkfWvH3LFig182fEBXYGdcBQ2bHBIvWtepx8eh5RiLyCLU38WtVGE7ESRtVrPT0GXXiXSACg6mL4sbxjsoznkkjLyy7Z2O0QeXY5ImnlF62joh"}
        response = requests.get(PRODUCTS_URL, cookies=cookies)
        for response in response.json():
            product_list.append(product(response))
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

