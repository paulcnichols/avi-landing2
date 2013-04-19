# Create your views here.
from collector.models import *
from django.views.generic.edit import CreateView
#from collector.forms import InterestedForm
#from django.views.generic.edit import FormView
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
import smtplib

class InterestedView(CreateView):# FormView):
    #form_class = InterestedForm
    model = Interested

    def form_invalid(self, form):
        return HttpResponseRedirect('/')
    
    def form_valid(self, form):
        message = \
"""From: Potential Customer <landing@avinetworks.com>
To: Paul Nichols <pnichols@avinetworks.com>, Guru Chahal <guru@avinetworks.com>
Subject: [interested] - %s

""" % (form.cleaned_data['email'])
        s = smtplib.SMTP('localhost')
        s.sendmail('landing@avinetworks.com', 'pnichols@avinetworks.com', message)
        s.quit()
        return HttpResponseRedirect('/')

    @csrf_exempt
    def dispatch(self, *args, **kwargs):
        return super(InterestedView, self).dispatch(*args, **kwargs)
