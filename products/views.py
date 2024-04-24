from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.forms import modelformset_factory
from .models import Item, Bill
from .admin import BillForm  # Assuming you have a BillForm as defined earlier

@login_required
def manage_items(request):
    items = Item.objects.all()
    return render(request, 'manage_items.html', {'items': items})

@login_required
def create_bill(request):
    if request.method == 'POST':
        form = BillForm(request.POST)
        if form.is_valid():
            new_bill = form.save(commit=False)
            new_bill.save()  # Save the Bill to generate its ID.
            form.save_m2m()  # Link the selected items to the Bill.

            # Explicitly call save to trigger total_cost calculation.
            new_bill.save()  
            return redirect('bill_detail', bill_id=new_bill.id)
    else:
        form = BillForm()
    return render(request, 'create_bill.html', {'form': form})

@login_required
def bill_detail(request, bill_id):
    bill = Bill.objects.get(id=bill_id)
    return render(request, 'bill_detail.html', {'bill': bill})
