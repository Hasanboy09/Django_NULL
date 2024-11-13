import os

import django
from django.db.models import Q
from django.db.models.aggregates import Sum

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
