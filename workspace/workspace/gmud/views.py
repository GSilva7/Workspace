from django.shortcuts import render, redirect, get_object_or_404

from workspace.settings import MEDIA_ROOT
from .models import gmud
from .forms import GmudCreateForm, GmudUpdateForm, GmudEndForm
from django.forms import ModelForm
# Create your views here.


def GmudList(request, template_name='gmud/gmud_list.html'):
    Gmud = gmud.objects.all()
    data = {}
    data['object_list'] = Gmud
    return render(request, template_name, data)

def GmudCreate(request, template_name='gmud/gmud_form.html'):
    form = GmudCreateForm(request.POST or None, request.FILES)
    if form.is_valid():
        form.save()
        save_file(request.FILES['procedimento'])
        return redirect('gmud_list')
    form = GmudCreateForm()
    return render(request, template_name, {'form':form})

def GmudView(request, pk, template_name='gmud/gmud_detail.html'):
    Gmud = get_object_or_404(gmud, pk=pk)
    return render(request, template_name, {'object':Gmud})

def GmudUpdate(request, pk, template_name='gmud/gmud_form.html'):
    Gmud = get_object_or_404(gmud, pk=pk)
    form = GmudUpdateForm(request.POST or None, instance=Gmud)
    if form.is_valid():
        form.save()
        return redirect('gmud_list')
    return render(request, template_name, {'form':form})
def GmudEnd(request, pk, template_name='gmud/gmud_end.html'):
    Gmud = get_object_or_404(gmud, pk=pk)
    form = GmudEndForm(request.POST or None, instance=Gmud)
    if form.is_valid():
        form.save()
        return redirect('gmud_list')
    return render(request, template_name, {'form':form})

def save_file(file, path=''):
    ''' Little helper to save a file
    '''
    filename = file._get_name()
    fd = open('%s/%s' % (MEDIA_ROOT, str(path) + str(filename)), 'wb')
    for chunk in file.chunks():
        fd.write(chunk)
    fd.close()