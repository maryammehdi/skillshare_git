from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from drinkers.forms import RegistrationForm
from drinkers.models import Drinker
# Create your views here.
def DrinkerRegistration(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/admin/')
    if request.method == 'POST': # submitting the form back
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(username=form.cleaned_data['username'], email = form.cleaned_data['email'],
                                            password = form.cleaned_data['password'])
#            user.save()
#            drinker = user.get_profile()
#            drinker.name = form.cleaned_data['name']
#            drinker.birthday = form.cleaned_data['birthday']
#            drinker.save()
#            drinker.save()
            drinker = Drinker(user=User, name=form.cleaned_data['name'], birthday=form.cleaned_data['birthday'])
            drinker.save()
            return HttpResponseRedirect('/profile/')
        else:
            return render_to_response('register.html', {'form': form}, context_instance=RequestContext(request))
        
        
        
    else: #showing the form
        '''users not submitting form, show them a blank registration form'''
        form = RegistrationForm()
        context = {'form': form}
        return render_to_response('register.html', context, context_instance=RequestContext(request))
    
        