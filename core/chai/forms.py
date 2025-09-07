from django import forms 

class modelForm(forms.Form):
    num1 = forms.IntegerField(
        label="Value1",
        max_value=1001,
        required=True,
        widget=forms.NumberInput(attrs={
            "id": "num1",
            "class": "w-full text-black border border-gray-300 rounded-md px-3 py-2 "
                     "focus:outline-none focus:ring-2 focus:ring-orange-400 focus:border-orange-400",
            "placeholder": "Enter Value1"
        })
    )

    num2 = forms.IntegerField(
        label="Value2",
        max_value=1001,
        required=True,
        widget=forms.NumberInput(attrs={
            "id": "num2",
            "class": "w-full text-black border border-gray-300 rounded-md px-3 py-2 "
                     "focus:outline-none focus:ring-2 focus:ring-orange-400 focus:border-orange-400",
            "placeholder": "Enter Value2"
        })
    )
