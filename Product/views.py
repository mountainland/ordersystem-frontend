from django.views.generic import DetailView, ListView, UpdateView, CreateView, TemplateView
from .models import Product, Order, Payment_method, City
from .forms import OrderForm
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.admin.views.decorators import staff_member_required
import requests
import json
from django.template.defaulttags import register
PRODS = []

BACKEND_URL = "https://botsarefuture-solid-happiness-p56jq4j774xh97p5-8000.preview.app.github.dev"

#@method_decorator(login_required, name='dispatch')
def ProductListView(request):
    #product_list = Product.objects.all()
    import requests

    url = "https://botsarefuture-solid-happiness-p56jq4j774xh97p5-8000.preview.app.github.dev/ordersystem/api/products/?format=json"

    payload={}
    headers = {
    'Cookie': '__Host-vso-pf=04E0A8DA375533E14286EECFAC82B63E%3Aj3Ni3C%2FPu4xIhwD48bThu68zq8GjLBt3TcHx%2Fxz0ZDEfdeCpi3%2FHUUhnIdX2BuhvXF0iiYBtsu9ATsHhat99EAZ0Oo3EZ76tN58QyGkRIqeogNapr7K3LuNpmFiVimWQc8onKECjqnKwm0ye2GcWJ9GLR2755jtFpN3HkpcCWbfwpPgVZlDg9jrZsppe%2BebOCih%2FSGJ0DJQduionUu9C4O6WsJH%2BWOYDfHdPp3nWYt%2BpcdNi22z55WAhZQqaO54Z8e5pgFFcIV%2BkGXoPJ3fsHCIaCmD0doxv6NyRuZfA3qcNtz8y5xj07Jy69iF5Vna1PxbWmF7KXm44noxzh6ivkCz%2BKXy1tWHOiJGzUFOVJTb3VNVnOm3ZW29vt%2FvpaYRk7N2Jdxy5D82j3nDL%2BglAzlOSQzaVFqkXi1Wszo120b2CBL2e91zGGkMFWbaawn3vDghxz1Zx9zW9gfnp8ynWbWfHUQpHxNVEJzmmA4d84DHqgt%2FB4pSDYzMJZ5okGGphnaOjWdTp1i%2FTQSzxi8bCJl3F0pFPKM8xxSzqY6trQfjujlmUJrc9%2FxFHPtkCFXm4ZNNCAZaT6N4WMQC%2BpZNCer9pEor8eyTCHvPrPAbrMeKA7FEu1VBZPLQam6E4whZDKTbsTgqFnYZILesOsr5Y81VTU2L4jCHjfjaR0xKbux5mIaEQM0gWa8ctg%2BnumUeE2Y7sIX7qB07eE0c3qiV9ZkxY0lYmn6gq7BnJJbUnk4CvoNCxWzZBtfFatOFo6IGEYZRhpQU0k5F%2BEdn0Xm0XBIudZ5eDRZeAqqhjC96tt4r5usxxhAgUggKAUyjrxNp2Hu%2FMKqoS1GrrVoiV3kPNDOivIln2Snxz5TdYcD%2FMfbnnuboGV6OZA%2FdW8qSrlRGh%2BICnoeP%2BxLoHISwUPUMM4G29oEN5MQQX9rbVgv5LioClinmiWHlSOitIoDQ8bAnQ%2FGI7DiaAvpjGR8XDgNOK1pkbRFvLvFhCj01h%2B91R1ikQXE6H7Th92RDKtsHy1gsxBOrks5s50sUZ0IlV2hAbD4%2B81na3pOhHxMF15seDWJ4bmhoAomZvMn4nptUEcEO7XG%2BxUTCx3gqrI%2Bvkv64mY2aJrGT7ajzXyWHLQDAW74M1ObRx7loUzWxcvWdDPATGxvwPT7o3pgjV6XqUXuAIrSotl6nyJZnFuqfif7sJH6fMUv2zA5jFeAWXmNNsNn%2FEiOyjqJPOgLeyoPUzBstZLBD0YortjjufecfXFJxo0GxUtl3qV54wXpcHlpbpqE3SgMdAglysoAWmzqM98GBeIng62ChJwyKnrCEzkewVj23TgMkuAG2CMgdWjtDDax8ebAT5rJV%2BY1CLcF2qtEDH4QKRoR6dLbVzamOKeHmOA0CA4mRvqi6Y51pUIToPL%2FKjwjn5f3evJVnzBLPtRMHijwOub9Cp0FNJviuyMNElnw8y2id%2Bt89S%2BTDB%2BXBwChaJ6uPFbCn%2F84YUmp1DOx3pD6TwJB%2Bb7ZSh9GZRYw76%2F8WNichCxmrcdBU6Q%2FdVSziFDB%2BVEjw05JRqQWKEfhzQ5NFjc31Ki1s79MRAN5w%2FmJVoVLwIFp9BFxMhAFZKxRI9uNFfpuXEAHLbS3zsxflefchkckAkUf4T8L3jLGmZ6FCnrWADkPw0n0%2Bqr%2BTCFH8qKaABvKQCoB9oNaXISZABfBpQclAsfM%2FFypv%2BhSd%2BjaNrlXk%2FcqasdOmMELum6FcPjQEo4FSIOVjltbQPvYg8dHQLBaeVWt1Km4i697cEv5B%2BNFowPVnn2e8CTh6aAUYpwmI1ygEoP1MAVWAiipakgEcfKmTHO6ILHFJMJvB9YxsPUrJrO4VrI53K6x7zhV%2B0gjpF4d1wuJ1nyxeDlEHRMYuB50KkRJHW1rSfvbd23Uysgxm1xBoDcwY%2B%2FoX%2FtMOoz2UDlPqc6hvK5OU6hFp6bXI%2BTBLuk4tfNp0qApCquy%2BaiM%2BdnwUYDl6vXpm6CKwIEnpDGBUtTVtXN7bXPTnAYUNXaeeFfmK%2BeR6UBvc7aG%2FbetDpYyYkUKEZulGY9wnv9jCOCGToqaXg8o3ZYZFRwKRqNVftJFwTiFWO1C5M%2FcpZaMJkhZojPTz%2FUZNb92p4EA1hjQt%2BLXFLkhrvZORnMbpJKWnuTwo57r5TyCSMV7hgW2%2B42f0anABZn98%2BJEcp7XjblonfbhEagXS41yFgxi2qrIMbIDf9KXB7MUAqgWM%2BASydQnVzkPATaMfY1EISuAg0VG0p8gArAHgGRk0z8cHAEh1MtBHpTT0dt4BjdX0ZqgBaeosZcH%2FLpXS0V7HiKNQWlTRJXZSAQFcXg9JiINMme5iebuf4mFTYJxszZwLmiVof3zSvRzRHcHCuRl2s8tgOqIagbDPvhrJynqLMF3mgbPDLCUqbYriq8D7Echd9r3EP%2FvBCGMV0jLIBXaaXSondfGZJmQcSrxD75%2FGZJhS9RTCd8PQEDuwvnkLu%2B738dPDnLVoU%2Bux53ZMb8TPP; codespaces_correlation_id=0afdc2f592ecba1285ced434ce26520c'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    products = response

    print(products.text)
    products_data = products.json()
    context = {'object_list': products_data}
    return render(request, 'product_list.html', context)

@register.filter
def get_value(dictionary, key):
    return dictionary.get(key)

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

