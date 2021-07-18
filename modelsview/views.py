from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from .models import Items
from django.db.models import Max, Count, Sum
from django import forms


# Create your views here.

class ItemsForm(forms.ModelForm):
    class Meta:
        model = Items
        fields = "__all__"

def index(request):
    return render(request, "index.html", {"view": True})


def AddItemView(request):
    totalCost = Items.objects.aggregate(Sum('total_cost'))
    distinct = Items.objects.values('item_name').distinct()
    return render(request, "index.html", {"addItem": True, "totalCost": totalCost, "items": distinct})

def addItem(request):
    if request.method == "POST":
        item_id = request.POST['item_id']
        item_name = request.POST['item_name']
        rate = request.POST['rate']
        quantity = request.POST['quantity']
        total_cost  = request.POST['total_cost']
        formData = Items(item_id=item_id, item_name=item_name, rate=rate,quantity=quantity, total_cost=total_cost)
        try:
            formData.save()
            return render(request, "index.html", {"addItem": True,"msgItem":"Item Saved Successfully"})
        except:
            return render(request, "index.html", {"addItem": True, "errMsgItem": "Something Gone wrong"})
    else:
        return render(request, "index.html", {"addItem": True})
    return render(request, "index.html", {"addItem": True})

def listView(request):
    totalCost = Items.objects.aggregate(total=Sum('total_cost'))
    # distinct = Items.objects.values('item_name').distinct()
    items = Items.objects.all()
    return render(request, 'lists.html', {"totalCost": totalCost['total'], "items": items})

def getListItems(request):
    totalCost = Items.objects.aggregate(Sum('total-cost'))
    items = Items.objects.all()
    # distinct = Items.objects.values('item_name').distinct()
    # distinct = Items.objects.values(
    #     'item_name'
    # ).annotate(item_count=Count('item_name')).filter(item_count=1)
    # records = Items.objects.filter(first_name__in=[item['item_name'] for item in distinct])
    return render(request, "index.html", {"totalCost": totalCost,"items":items})

def edit(request,id):
    item = Items.objects.get(id=id)
    return render(request, 'edit.html', {'editItem': item})

def update(request,id):
    item = Items.objects.get(id=id)
    form = ItemsForm(request.POST, instance=item)
    if form.is_valid():
        form.save()
        return redirect('/list-view/')

def searchByItemName(request):
    totalCost = Items.objects.aggregate(total=Sum('total_cost'))
    # distinct = Items.objects.values('item_name').distinct()
    items = Items.objects.filter(item_name__icontains=request.POST.get('search-item'), quantity__gte=1, quantity__lte=10).all()
    print(items)
    return render(request, 'lists.html', {"totalCost": totalCost['total'], "items": items})
