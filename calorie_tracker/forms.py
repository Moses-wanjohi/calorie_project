from django import forms
from .models import FoodItem


class FoodItemForm(forms.ModelForm):
    """
    Form for adding a new FoodItem with custom Tailwind CSS widget attributes.
    """
    class Meta:
        model = FoodItem
        fields = ['name', 'calories']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2.5 bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-2 focus:ring-emerald-500 focus:border-emerald-500 block text-sm transition',
                'placeholder': 'e.g., Avocado Toast with Eggs',
                'required': 'required',
            }),
            'calories': forms.NumberInput(attrs={
                'class': 'w-full px-4 py-2.5 bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-2 focus:ring-emerald-500 focus:border-emerald-500 block text-sm transition',
                'placeholder': 'e.g., 350',
                'min': '1',
                'required': 'required',
            }),
        }