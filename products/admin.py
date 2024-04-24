from django import forms
from django.contrib import admin
from .models import Item, Bill

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = '__all__'
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4, 'cols': 40}),  # Makes the description field larger
        }

class BillForm(forms.ModelForm):
    items = forms.ModelMultipleChoiceField(
        queryset=Item.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )

    class Meta:
        model = Bill
        fields = ['items']

class ItemAdmin(admin.ModelAdmin):
    form = ItemForm
    list_display = ('name', 'price', 'description')
    search_fields = ('name', 'description')

admin.site.register(Item, ItemAdmin)

class BillAdmin(admin.ModelAdmin):
    list_display = ['id', 'total_cost']
    filter_horizontal = ('items',)  # This provides a widget to select multiple items easily

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        obj.total_cost = sum(item.price for item in obj.items.all())
        obj.save()

admin.site.register(Bill, BillAdmin)
