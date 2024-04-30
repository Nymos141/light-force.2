from django import forms
from game.models import Feedback
class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={'rows': 4, 'cols': 50, 'placeholder': 'Комментарий'}),
            }
