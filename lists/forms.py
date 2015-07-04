from django import forms
from lists.models import Item


class ItemForm(forms.models.ModelForm):

    class Meta:
        model = Item
        fields = ('text',)
        widgets = {
            'text': forms.fields.TextInput(attrs={
                'placeholder': 'Enter a To-Do item',
                'class': 'form-control input-lg',
            }),
        }
