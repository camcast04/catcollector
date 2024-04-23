from django.shortcuts import render
from .models import Cat
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# TODO temporary database -> remove this after adding cat model

cats = [
    {'name': 'Lolo', 'breed': 'tabby', 'description': 'furry little demon', 'age': 3},
    {'name': 'Sachi', 'breed': 'calico', 'description': 'gentle and loving', 'age': 2},
]


# Create your views here.
def home(request):
    return render(request, 'home.html') #second argument is the string the represents out template (html file)

def about(request):
    return render(request, 'about.html' )

# def cats_index(request):
#     return render(request, 'cats/index.html', {
#         'cats':cats
#     })

def cats_index(request):
  cats = Cat.objects.all()
  return render(request, 'cats/index.html', { 'cats': cats })

def cats_detail(request, cat_id):
    #we need to communicate with the databse here 
    #return result of redering a template
    cat = Cat.objects.get(id = cat_id)
    return render(request, 'cats/detail.html', {
        'cat':cat
    })
    
    
class CatCreate(CreateView):
    model = Cat
    fields = '__all__'
    # success_url = '/cats/' # not reccomended / not best practice 
    
class CatUpdate(UpdateView):
    model = Cat
    fields = ('description', 'age')

class CatDelete(DeleteView):
    model = Cat
    success_url = '/cats/'