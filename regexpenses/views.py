from django.shortcuts import render, get_object_or_404, redirect
#from django.utils import timezone
from .models import expenses, daily_target
from .forms import regExp
from django.core.paginator import Paginator
from datetime import date, timedelta
#from django.contrib import messages
#from django.db.models import Q



def index(request):
    user = request.user
    if user.is_authenticated:
        page = request.GET.get('page', '1')
        kw = request.GET.get('kw', '')  # 검색어
        kw_type = request.GET.get('type','')
        data = expenses.objects.filter(amtdate__range=[date.today() - timedelta(days=60), date.today()]).values().all()
        if kw:
            if kw_type == 'category':
                data = expenses.objects.filter(cat = kw)
            elif kw_type == 'subject':
                data = expenses.objects.filter(subject = kw)
            elif kw_type == 'date':
                data = expenses.objects.filter(amtdate = kw)
        paginator = Paginator(data, 15)  # 페이지당 15개씩 보여주기
        page_obj = paginator.get_page(page)
        context = {'exp_list': page_obj, 'page':page, 'kw':kw, 'kw_type':kw_type}
        return render(request, 'regexpenses/exp_list.html', context)
    else:
        return redirect('common:login')


def add_data(request):
    tamt = expenses.objects.filter(id=1)
    if request.method == 'POST':
        form = regExp(request.POST)
        if form.is_valid():
            datas = form.save(commit=False)
            datas.save()
            listup = regexpenses.objects.filter(id=reg_id)
            context = {'exp_list': listup,'cond':False,'tamt':tamt}
            return render(request, 'regexpenses/exp_list.html', context)
    else:
        form = regExp()
        context = {'form': form,'cond':False,'tamt':tamt}
        return render(request, 'regexpenses/detail.html', context)


def detail(request,reg_id):
    tamt = expenses.objects.filter(id=1)
    data = get_object_or_404(expenses, pk=reg_id)
    if request.method == 'POST':
        form = regExp(request.POST, instance=data)
        if form.is_valid():
            datas = form.save(commit=False)
            datas.save()
            listup = regexpenses.objects.filter(id=reg_id)
            context = {'exp_list': listup,'cond':True}
            return render(request, 'regexpenses/exp_list.html', context)
    else:
        form = regExp(instance=data)
        context = {'form': form,'cond':True,'tamt':tamt}
        return render(request, 'regexpenses/detail.html', context)

def delete(request,reg_id):
    pass