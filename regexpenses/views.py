from django.shortcuts import render, get_object_or_404, redirect
#from django.utils import timezone
from .models import expenses
#from .forms import bom1Forms
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
                data = expenses.objects.filter(jepum_code = kw, seq = '1')
            elif kw_type == 'subject':
                data = expenses.objects.filter(jaje_code = kw)
            elif kw_type == 'date':
                data = expenses.objects.filter(pumname = kw)
        paginator = Paginator(data, 15)  # 페이지당 15개씩 보여주기
        page_obj = paginator.get_page(page)
        context = {'exp_list': page_obj, 'page':page, 'kw':kw, 'kw_type':kw_type}
        return render(request, 'regexpenses/exp_list.html', context)
    else:
        return redirect('common:login')


def