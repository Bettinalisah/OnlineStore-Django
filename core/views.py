from django.shortcuts import render, redirect
from item.models import Category, Item
from .forms import SignupForm
from PIL import Image
import os

def resize_image(image_path, size=(5536, 4160)):
    with Image.open(image_path) as img:
        resized_img = img.resize(size)
        resized_img.save(image_path)

def index(request):
    items = Item.objects.filter(is_sold=False)[:6]
    categories = Category.objects.all()

    for item in items:
        path = os.path.join(os.getcwd(), item.image.url.lstrip('/'))
        resize_image(path)

    return render(request, 'core/index.html', {
        'categories': categories,
        'items': items,
    })

def contact(request):
    return render(request, 'core/contact.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')
    else:
        form = SignupForm()

    return render(request, 'core/signup.html', {
        'form': form
    })
