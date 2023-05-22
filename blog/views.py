from django.shortcuts import render

# Create your views here.
def post_list(request):
    return render(request, 'blog/post_list.html', {})

def yun_dongju(request):
    return render(request, 'blog/yun_dongju.html', {})
