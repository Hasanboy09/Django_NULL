import os

import django
from django.db.models import Q, Value
from django.db.models.aggregates import Sum
from django.db.models.fields import CharField

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



from apps.models import Product, Category


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



# ==============================================  defer  ===============================================
from apps.models import Product

product_id = input('id: ')
products = Product.objects.raw("select * from product where id=%s" % product_id)
for product in products:
    print(product.name , product.price)