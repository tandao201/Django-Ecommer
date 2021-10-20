from django.db.models.query_utils import Q
from django.shortcuts import render
from store.models import Product, Category
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
def home(request):
    allProducts = Product.objects.all()
    allCategories = Category.objects.all()
    category_id = request.GET.get('category', None)
    if category_id is not None:
        allProducts = Product.getProductByID(category_id)
    data = {
        'products' : allProducts,
        'categories' : allCategories
    }
    return render(request, 'index.html', data)

def search(request):
    q = request.GET['q'].title()
    data = Product.objects.filter(name__icontains=q).order_by('id')
    return render(request, 'search-result.html', {'data': data})

def detail(request, pk):
    product = Product.objects.get(id = pk)
    context = {'product' :product}
    return render(request, 'product-detail.html', context )

def contact(request):
    return render(request, 'another/contact.html')
