from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import NameForm
import logging

logger = logging.getLogger(__name__)
def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            logger.debug(form.cleaned_data['your_name'])
    else:
        form = NameForm()
    
    context = {}
    context['form'] = form
    return render(request, "ex02/form.html", context)