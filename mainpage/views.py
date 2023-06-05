from django.shortcuts import render, get_object_or_404, redirect

def index(request):
    user =request.user
    if user.is_authentificated:
        return redirect('regexpenses:index')
    else:
        return redirect('common:login')