from django.shortcuts import render
from django.http import Http404
from django.http.response import HttpResponseRedirect
from django.views.generic import CreateView, ListView, DetailView, UpdateView
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin


from .forms import NotesForm
from .models import Notes


class NotesDeleteView(DeleteView):
    model = Notes
    success_url = '/notes/notes'
    template_name = 'notes/notes_delete.html'


class NotesUpdateView(UpdateView):
    model = Notes
    success_url = '/notes/notes'
    form_class = NotesForm
    #template_name = ''


class NotesCreateView(CreateView):
    model = Notes
    success_url = '/notes/notes'
    form_class = NotesForm
    login_url = '/login/'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class NotesView(LoginRequiredMixin, ListView):
    model = Notes
    context_object_name = 'notes'
    template_name = 'notes/getall.html'
    #login_url = '/admin'
    login_url = '/login'

    def get_queryset(self):
        return self.request.user.notes.all()


class DetailView(DetailView):
    model = Notes
    context_object_name = 'note'
    template_name = 'notes/notes_detail.html'

# def notes(request):
#     notes=Notes.objects.all()
#     return render(request, 'notes/getall.html', {'notes':notes})

# def detail(request, pk):
#     try:
#         note=Notes.objects.get(pk=pk)
#     except Notes.DoesNotExist:
#         raise Http404("Note doesn't exist.")
#     return render(request, template_name='notes/notes_detail.html',
#                   context={
#                       'note':note
#                    })
