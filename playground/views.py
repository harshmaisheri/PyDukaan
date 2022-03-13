from django.shortcuts import render
from django.contrib.contenttypes.models import ContentType
from store.models import Product
from tags.models import TaggedItem


def say_hello(request):
    # queryset = Product.objects.filter(
    #     id__in=OrderItem.objects.values('product_id').distinct()).order_by('title')

    # queryset = Product.objects.prefetch_related(
    #     'promotions').select_related('collection').all()

    # queryset = Order.objects.select_related(
    #     'customer').prefetch_related('orderitem_set__product').order_by('-placed_at')[:5]

    TaggedItem.objects.get_tags_for(Product, 1)

    return render(request, 'hello.html', {'orders': list(queryset)})
