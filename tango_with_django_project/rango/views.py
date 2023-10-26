from django.shortcuts import render
from rango.models import Category


def index(request):
    context_dict = {
        'aboldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'
    }
    category_list = Category.objects.order_by('-likes')[:5]
    context_dict['categories'] = category_list
    return render(request, 'rango/index.html', context=context_dict)


def about(request):
    return render(request, 'rango/about.html', context={})
