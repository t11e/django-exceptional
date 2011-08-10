from django.conf.urls.defaults import *
from djexceptional import Exceptional
from django.http import HttpResponse
import sys, traceback

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()


def just_raise(request):
    def f():
        def g():
            raise ValueError("We've run out of Venezuelan Beaver Cheese.")
        g()
    return f()
    
def raise_manually(request):
    text = "Our supply of Peruvian Monkey Brains is depleted."
    send_exception(text)
    return HttpResponse("Just sent an exception manually to Exceptional: %s" % text)

def send_exception(text):
    try:
        send_exception2(text)
    except ValueError as v:
        e = Exceptional()
        e.send(v,{'extra':'extra_value','another':'another_extra_value'})
    
def send_exception2(text):    
    raise ValueError(text)
        
urlpatterns = patterns('',
    # Example:
    # (r'^example/', include('example.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
    (r'^$', just_raise),
    (r'^manually$', raise_manually),
)
