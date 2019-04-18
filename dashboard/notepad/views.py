from django.shortcuts import render, redirect

from .forms import NoteModelForm
from .models import Note

from django.views.generic import DetailView
# Create your views here.

def create_view(request):

    form = NoteModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.instance.user = request.user
        form.save()
        return redirect('/notes/list/')

    context = {
        'form': form
    }
    
    return render(request, "notepad/create.html", context)

def list_view(request):
    notes = Note.objects.all()
    context = {
        'object_list': notes
    }
    return render(request, "notepad/list.html", context)

def delete_view(request, id):
    item_to_delete = Note.objects.filter(pk=id)
    if item_to_delete.exists():
        if request.user == item_to_delete[0].user:
            item_to_delete[0].delete()
    return redirect('/notes/list')

class NoteDetailView(DetailView):
    model = Note



'''
def note_detail(request, pk):
    note = get_object_or_404(Note, pk=pk)
    note_pk = note.title.pk
    return redirect('note_detail', pk=note_pk)

    comment = get_object_or_404(Comment, pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('post_detail', pk=post_pk)
'''