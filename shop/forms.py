from django import forms

from .models import *

class CreateShopForm(forms.ModelForm):
    class Meta:
        model = Shop
        fields = ['shop_name', 'slug', 'shop_description',
                  'sell_services', 'sell_products','banner']
        widgets = {
            'slug': forms.TextInput(attrs={'class': '',
                                           'placeholder': " до 50 символов"}),
            'shop_name': forms.TextInput(attrs={'class': '',
                                            'placeholder': " до 50 символов"}),
            'shop_description': forms.Textarea(attrs={'cols': 60,
                                    'rows': 5, 'placeholder': " до 500 символов"}),
        }


class AddProductForm(forms.ModelForm):
    def __init__(self, *args, **kwards):
        super().__init__(*args, **kwards)
        self.fields['categor'].empty_label = "Категория не выбрана"

    class Meta:
        model = Product
        fields = ['categor', 'title', 'price', 'product_description', 'is_published', 'status', 'main_photo', 'photo1',
                  'photo2', 'photo3']
        widgets = {
            'title': forms.TextInput(attrs={'class': '', 'placeholder': " до 50 символов"}),
            'price': forms.TextInput(attrs={'class': '', 'placeholder': " до 50 символов"}),
            'product_description': forms.Textarea(attrs={'cols': 60, 'rows': 10, 'placeholder': " до 500 символов"}),
        }

