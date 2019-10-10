from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product
from django.utils import timezone

from .models import Product
# Create your views here.

def product_list(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'pro':products})

@login_required
def publish(request):
    if request.method == 'GET':
        return render(request,'publish.html')
    elif request.method == 'POST':
        title = request.POST['APP名称']
        intro = request.POST['介绍']
        try:
            icon = request.FILES['APP图标']
            image = request.FILES['大图']
            if title and intro and icon and image:
                product = Product()
                product.title = title
                product.intro = intro
                product.icon = icon
                product.image = image
                product.pub_date = timezone.datetime.now()
                product.hunter = request.user
                product.save()
                return redirect('主页')

        except Exception as err:
            return render(request,'publish.html',{'图片错误':'请上传图片'})

def detail(request, product_id):
    product = get_object_or_404(Product,pk=product_id)
    return render(request,'detail.html',{'product':product})