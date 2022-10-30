from django import forms
from .models import Product, Order

class OrderForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control',})
        self.fields['contact'].widget.attrs.update({'class': 'form-control'})
        self.fields['address'].widget.attrs.update({'class': 'form-control',})
        self.fields['postcode'].widget.attrs.update({'class': 'form-control',})
        self.fields['city'].widget.attrs.update({'class': 'form-control'})
        self.fields['information'].widget.attrs.update({'class': 'form-control'})
        self.fields['payment_method'].widget.attrs.update({'class': 'form-control'})

        
        self.fields['count_1'].widget.attrs.update({'class': 'form-control'})
        self.fields['count_2'].widget.attrs.update({'class': 'form-control'})
        self.fields["count_3"].widget.attrs.update({'class': 'form-control'})


        self.fields["product_1"].widget.attrs.update({'class': 'form-control'})
        self.fields["product_2"].widget.attrs.update({'class': 'form-control'})
        self.fields["product_3"].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Order
        fields = ['count_1', 'count_2', 'count_3', 'product_1', 'product_2', 'product_3', 'name','contact','address', 'postcode', 'city', 'information','payment_method',]
