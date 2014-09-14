# Create your views here.
#import sys
from django.shortcuts import render_to_response
from links.models import Link
from links.forms import LinkForm
from django.http import HttpResponseRedirect
#from django.core.exceptions

def submit(request):
    if request.method == 'POST':
        form = LinkForm(request.POST)
        if form.is_valid():
            #try:
            #    Link.objects.get(url=form.url)
            #except DoesNotExist:  
            instance = form.save()
            #instance.project = Link.objects.get(title=offset)
            instance.save()
            return HttpResponseRedirect('/')
    else:
        form = LinkForm()

    return render_to_response('links/submit.html', {'form': form})