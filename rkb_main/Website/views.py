from django.shortcuts import render
from django.http import HttpResponse

product_type=[
    {
        'name':'Boxing Shoes',
        'sizes':'9,9.5,10,10.5,11,12',
        'colorwave': 'SaSN Red and Black',
        'cost':'$106.99',
        'shipping':'$17',
        'totalCost':'$124.99'

    },
    {
        'name':'Running Belt',
        'sizes':'One size fits all',
        'colorwave': 'SaSN Red, Black, white',
        'cost':'21.99',
        'shipping':'$10',
        'totalCost':'$31.99'
    }
        
]

# Create your views here.
def home(request):
    context = {'is_home_page': True}
    return render(request, 'Website/landingPage.html', context)

def about(request):
    return render(request, 'Website/about.html')

def products(request):
    context={
        'products':product_type 
    }
    return render(request, 'Website/products.html',context)