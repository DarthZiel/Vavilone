from django.shortcuts import render
from .forms import RecordIncomeForm
from django.views.generic import CreateView
from .models import Income
# Create your views here.
def index(request):
    return render(request, 'midas/index.html')

class CreateIncomeRecord(CreateView):
    form_class = RecordIncomeForm
    template_name = 'midas/create.html'
    success_url = '/'
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

