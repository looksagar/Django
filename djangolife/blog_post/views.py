from django.shortcuts import render
from .models import post
# Create your views here.

def home(request):
    all_post = post.objects.all()
    #print(all_post)
    for po in all_post:
        print(po)
    return render(request, 'index.html', {'all_post_list': all_post})

    #return render(request, 'index.html',{'name':"SAGAR CHANDRA CHANDA",'district':"CHANDPUR"})



def post_list(request):
    post_list = post.objects.all()
    return render(request, 'post_list.html', {'post_list': post_list})


def single_post(request, post_id):
    posts = post.objects.get(pk=post_id)
    print(posts)
    return render(request, 'single_post.html', {'post':post})