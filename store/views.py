from django.db import models
from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Category, Product
import json
import datetime
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from .models import *
# Create your views here.
class store(View,LoginRequiredMixin):
	def get(self,request):
		allProducts = Product.objects.all()
		allCategories = Category.objects.all()
		category_id = request.GET.get('category', None)
		if category_id is not None:
			allProducts = Product.getProductByID(category_id)
		# count = len(allProducts)
		page = request.GET.get('page')
		page = page or 1
		paginator = Paginator(allProducts, 6)
		paged_products = paginator.get_page(page)
		product_count = allProducts.count()

		data = {
			'products' : paged_products,
			'categories' : allCategories,
			'product_count': product_count,
		}
		return render(request, 'store.html', data)
