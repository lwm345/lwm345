from django.shortcuts import render
from django.db import models
# Create your views here.
# 作者列表
import json

from django.shortcuts import render, HttpResponse
from user.models import Note


# Create your views here.
Å
# 主页面
def main_page(request):
    # 获取所有未被删除的文章
    notes = [i for i in Note.objects.exclude(status='D')]
    return render(request, 'main.html', {'note': notes})



def add_note(request):
    data = json.loads(request.body)
    name, text, s_time, e_time = data.values()
    Note.objects.create(name=name, text=text, s_time=s_time, e_time=e_time, status='U')
    return HttpResponse(json.dumps({'result': 1}))


def modify_note(request):
    data = json.loads(request.body)
    n_id, name, text, s_time, e_time = data.values()
    Note.objects.filter(id=n_id).update(name=name, text=text,s_time=s_time, e_time=e_time)
    return HttpResponse(json.dumps({'result': 1}))


def del_note(request):
    data = json.loads(request.body)
    n_id = list(data.values())[0]
    Note.objects.filter(id=n_id).delete()
    if Note.objects.filter(id=n_id).exists():
        return HttpResponse(json.dumps({'result': -1}))
    return HttpResponse(json.dumps({'result': 1}))

def change_note_status(request):
    data = json.loads(request.body)
    n_id, status = data.values()
    Note.objects.filter(id=n_id).update(status=status)
    if Note.objects.filter(id=n_id, status=status).exists():
        return HttpResponse(json.dumps({'result': 1}))
    return HttpResponse(json.dumps({'result': -1}))

