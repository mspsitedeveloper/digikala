from .models import Product

def recent_products(request):
    recent = Product.objects.order_by("-date")[:4]
    return {"recent_products":recent}