from django.shortcuts import render


# Create your views here.
def basket_add(request, product_id):
    product = Menu.objects.get(id=product_id)
    basket, created = Menu.objects.get_or_create(user=request.user, product=product)
    if not created:
        basket.quantity += 1
        basket.save()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])