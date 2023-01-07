from django.http import HttpResponse
from django.shortcuts import render, redirect
from myapp.models import  *
from django.contrib import messages

def show_about_page(request):
    print("requesting show about page")
    name="Channel name is Learn Code with Durgesh"
    link="https://www.youtube.com/watch?v=697_0UGxDPk&t=182s"
    data={
        "name":name,
        "link":link
    }
    return render(request,"about.html",data)

def show_home_page(request):
    images = Image.objects.all()
    cats = Category.objects.all()
    data = {"images":images,"cats":cats}
    return render(request,"home.html",data)

def show_category(request,cid):
    cats = Category.objects.all()
    category=Category.objects.get(pk=cid)

    images = Image.objects.filter(cat=category)
    data = {"images": images, "cats": cats}
    return render(request, "home.html", data)

def home(request):
    return redirect('/home')

def search(request):
    query = request.GET['query']
    if len(query) > 78:
        images = Image.objects.none()
    else:
        imageTitle = Image.objects.filter(title__icontains=query)
        imageDescription = Image.objects.filter(description__icontains=query)
        images = imageTitle.union(imageDescription)

    if images.count() == 0:
        messages.warning(request,"No search results found. Please refine your query")
    cats = Category.objects.all()
    data = {"images": images,"cats": cats,"query":query}
    return render(request,"search.html",data)