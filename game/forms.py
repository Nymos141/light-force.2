from django import forms
from game.models import Feedback, Product

class FeedbackForm(forms.ModelForm):

    # def clean_text(self):
    #     text = self.cleaned_data.get('text')
    #     if text is None:
    #         raise forms.ValidationError("Введите комментарий")
    #     return text

    class Meta:
        model = Feedback
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={'rows': 4, 'cols': 50, 'placeholder': 'Комментарий'}),
        }


class ProductForm(forms.ModelForm):
    title = forms.CharField(max_length=60, min_length=3)
    text = forms.CharField(widget=forms.Textarea)
    image = forms.ImageField(required=False)
    price = forms.FloatField(required=False)

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price is not None and (price < 0 or price > 100.0):
            raise forms.ValidationError("Цена должна быть в пределах от $0 до $100.")
        return price

    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            "title": forms.TextInput(
                attrs={
                    "placeholder": "Введите название игры",
                    "class": "form-control"
                }
            ),

            "text": forms.Textarea(
                attrs={
                    "placeholder": "Введите описание игры",
                    "class": "form-control",
                    "rows": 4,
                    "cols": 50
                }
            ),

            "image": forms.FileInput(
                attrs={
                    "class": "form-control"
                }
            ),

            "price": forms.NumberInput(
                attrs={
                    "class": "form-control"
                }
            ),

            "tags": forms.SelectMultiple(
                attrs={
                    "class": "form-control"
                }
            )
        }
