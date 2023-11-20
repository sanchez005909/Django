from django import forms
from main.models import Product, Version, Category


class StyleFormMixin:
    def __init__(self, *args, **qwargs):
        super().__init__(*args, **qwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        exclude = ('datetime_create', 'is_published')

    def clean_title(self):
        cleaned_data = self.cleaned_data.get('title')
        prohibited_goods = ('казино', 'криптовалюта', 'крипта', 'биржа',
                            'дешево', 'бесплатно', 'обман', 'полиция', 'радар',)

        if cleaned_data.lower().strip() in prohibited_goods:
            raise forms.ValidationError(f'Нельзя добавить запрещенный продукт!\n'
                                        f'Запрещенные продукты: {prohibited_goods}')
        return cleaned_data


class VersionForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Version
        fields = ('num_version',
                  'name_version')


class CategoryForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name_category',
                  'description')
