import datetime

from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import expenses, daily_target
from .forms import regExp
from django.core.paginator import Paginator
from datetime import date, timedelta
from django.db.models import Count
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
                if kw == '기본식비(외식등)':
                    ids = 0
                elif kw == '유흥(놀고먹는거)':
                    ids = 1
                elif kw == '기타':
                    ids = 2
                data = expenses.objects.filter(cat = ids)
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
    tamt = daily_target.objects.all()
    mny = tamt[0].target
    if request.method == 'POST':
        form = regExp(request.POST)
        if form.is_valid():
            tdate = request.POST.get('adate')
            datas = form.save(commit=False)
            datas.save()
            return redirect('regexpenses:index')
    else:
        today = timezone.now().strftime('%Y-%m-%d')
        form = regExp()
        context = {'form': form,'cond':False,'tamt':mny,'adate':today}
        return render(request, 'regexpenses/detail.html', context)


def detail(request,reg_id):
    tamt = daily_target.objects.all()
    tamt = tamt[0].target
    data = get_object_or_404(expenses, pk=reg_id)
    if request.method == 'POST':
        form = regExp(request.POST, instance=data)
        if form.is_valid():
            datas = form.save(commit=False)
            datas.save()
            listup = expenses.objects.filter(id=reg_id)
            context = {'exp_list': listup,'cond':True}
            return render(request, 'regexpenses/exp_list.html', context)
    else:
        form = regExp(instance=data)
        lists = expenses.objects.filter(id=reg_id)
        adate = lists[0].amtdate
        adate = adate.strftime('%Y-%m-%d')
        context = {'adate':adate,'form': form,'cond':True,'tamt':tamt}
        return render(request, 'regexpenses/detail.html', context)

def input_tamt(request):
    tamt = daily_target.objects.all()
    if "GET" == request.method:
        mny = tamt[0].target
        context = {'tamt': mny}
        return render(request, 'regexpenses/input_amt.html',context)
    else:
        mny = request.POST["target_money"]
        del_data = tamt
        del_data.delete()
        datas = daily_target()
        datas.target = mny
        datas.save()
        context = {'tamt': mny}
        return render(request, 'regexpenses/detail.html', context)

