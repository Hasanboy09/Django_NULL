import os
from datetime import datetime

import django
from django.db import transaction
from django.db.models import Q, Value, F, Min
from django.db.models.aggregates import Sum, Count
from django.db.models.fields import CharField
from django.db.models.functions import Coalesce

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'root.settings')
django.setup()

# a = Category.objects.all()
# for i in a:
#     print(i.name)
#

# ===========================   filter ========================================


# from apps.models import Product
#
# a = Product.objects.filter(price__gte=50000)
# for i in a:
#     print(f"{i.name}" ,  i.price)


# ========================   exclude ===============================================


# from apps.models import Product
#
# a = Product.objects.exclude(Q(price=50000), Q(name__icontains='kitob'))
# for i in a:
#     print(f"{i.name}", i.price)

# ========================   annotate ===============================================

# from apps.models import Product
# from django.db.models import Count
#
# a = Product.objects.filter(category_id__gte=2).annotate(product_count = Sum('count'))
# for i in a:
#     print(i.count)


# ===================== alias ==============================================

# farqi annotate ustun yaratadi  , bu esa yoq


# ======================== Order by =============================================

# from apps.models import Product
# a = Product.objects.order_by('-price')
# for i in a:
#     print(i.name , i.price)


# ======================  distinct() ===========================================

# bir xil narxdagilarni bittasini oladi

# from apps.models import Product
# a = Product.objects.order_by('-price').distinct('price')
# for i in a:
#     print(i.name , i.price)


# ==========================   values() ==========================
# from apps.models import Product
# a = Product.objects.filter(price__gte=60000).values('name' , 'price')
#
# print(a)

# Natija:  [{'name': 'Teddy Ayiqcha', 'price': 60000}, {'name': 'Oq kema', 'price': 73000}, {'name': 'Oq kabutar', 'price': 65000}]>


# ===========================  values_list() ========================
# from apps.models import Product
# a = Product.objects.filter(name__icontains='oq').values_list('name', flat=True)
# print(a)

# Natija: <QuerySet ['Oq kema', 'Oq kabutar']>


# =============================  select_related() ==============================
# bazasidagi bog'langan ma'lumotlarni

# from apps.models import Product
# a = Product.objects.select_related('category').filter(price__gte=60000)
# for p in a:
#     print(p.name , p.category.name , p.price)

# Teddy Ayiqcha O`yinchoqlar 60000
# Oq kema Kitoblar 73000
# Oq kabutar Kitoblar 65000


# ===============================  prefetch related ================================
# Ko‘pdan-ko‘p bog‘lanishlar uchun (ManyToManyField


# ===========================  dates() ============================


from apps.models import Product, Category, User

# a = Category.objects.filter(name__icontains='texnika').values('name')
# b = Product.objects.filter(name__icontains='texnika').values('name')
# c= a.union(b)
# for item in c:
#     print(item.get('name'))


'''
Texnika 
yanig texnika
Eski texnika 

'''
#
#
# a = Category.objects.filter(name__icontains='texnika').values('name').annotate(source=Value('category', output_field=CharField()))
# b = Product.objects.filter(name__icontains='texnika').values('name').annotate(source=Value('product', output_field=CharField()))
#
# c = a.union(b)
#
# for item in c:
#     source = item.get('source')
#     name = item.get('name')
#     if source == 'category':
#         print(f"{name} (category)")
#     elif source == 'product':
#         print(f"{name} (product)")


# ==============================================  extra ===============================================
# from apps.models import Product
# products = Product.objects.extra(
#     where=["price > 140000"]
# )
#
# for product in products:
#     print(product.name)


# ==============================================  raw  ===============================================
# from apps.models import Product
#
# product_id = input('id: ')
# products = Product.objects.raw("select * from product where id=%s" % product_id)
# for product in products:
#     print(product.name , product.price)
#
#


# ==========================================  and  ================================================

# from apps.models import Product
# products = Product.objects.filter(Q(name__icontains='texnika') & Q(category__name__icontains='texnika'))
# for product in products:
#     print(product.name , product.price)
#


# ==========================================  or  ================================================

# from apps.models import Product
# products = Product.objects.filter(Q(name__icontains='texnika') | Q(category__name__icontains='texnika'))
# for product in products:
#     print(product.name , product.price)


# ==========================================  get_or_create()  ================================================

# from apps.models import Product
#
#
# obj,created = Product.objects.get_or_create(
#     name='Chayonlar vodiysi',
#     count=20,
#     category_id=1,
#
#     defaults={"name": "redmi"}
# )


# ========================================  bulk_create ==================================================

#  bitta query orqali ko`p yaratish imkonini beradi , save() ishlatilmaydi

# from apps.models import Product
#
# products = Product.objects.bulk_create(
#     [
#         Product(name='Choynik', price=25000, category_id=4, count=40, created_at=datetime.now()),
#         Product(name='piyola', price=5000, category_id=4, count=80, created_at=datetime.now()),
#     ]
# )
#
#


# products = [
#     Product(name=f"Product {i}", price=i * 10 , category_id=2 , count=i*2)
#     for i in range(1, 1001)
# ]
#
# # Ommaviy yaratish, har bir batch uchun 100 yozuv
# Product.objects.bulk_create(products, batch_size=100)

# batch_size -> har yaratganda nechta yaratib kelishi


# ======================= Task =======================

# ======= task 1

# from apps.models import Product
#
# product = Product.objects.filter(Q(category__name='meva') | Q(name='banan')).update(price = 25000)


# ====== task 2

# from apps.models import Product
#
# product = Product.objects.filter(category__name='meva').update(price = F('price' ) *2)


#  ===========================================  in_bulk =======================================




# from apps.models import Product
# product = Product.objects.in_bulk([1 ,4 ,6] , field_name='id')
#


#  ===========================================  iterator  =======================================

# from apps.models import Product
# a = Product.objects.iterator(chunk_size=2)
# for p in a:
#     print(p.name)


#  ===========================================  task  =======================================
# from django.db.models import F, Min, Sum
#
# price_min = Product.objects.aggregate(price_min=Min('price'))['price_min']
#
# if price_min is not None:
#     total_price = Product.objects.aggregate(total_price=Sum(F('price') + price_min))['total_price']
#     print(total_price)
# else:
#     print("Mahsulotlar mavjud emas yoki narxlar noto'g'ri.")



# task 1
# products = Product.objects.values('name', 'category').annotate(sum=Sum('price'))
# for i in products:
#     print(i)


# task 2
# products = Product.objects.values('name', 'category').annotate(sum=Sum('price') , product_count = Count('name'))
# for i in products:
#     print(i)


# task 3
# users = User.objects.filter(date_joined__year=2020)
#
# for user in users:
#     print(user.username)



# products = Product.objects.filter(price__range=(2000 , 3500)).filter(Q(description__isnull=False) & Q(name__icontains='a'))
# products = Product.objects.filter(price__range=(2000 , 3500), description__isnull=False, name__icontains='a')
# for product in products:
#     print(product.name)





