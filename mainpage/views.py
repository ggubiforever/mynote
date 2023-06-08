from django.shortcuts import render, get_object_or_404, redirect

def index(request):
    user = request.user
    if user.is_authenticated:
        return render(request,'mainpage/index_page.html')
    else:
        return redirect('common:login')