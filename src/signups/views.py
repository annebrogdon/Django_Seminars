from django.shortcuts import render, render_to_response, RequestContext, HttpResponseRedirect

# Create your views here.

from .forms import SignUpForm
from models import SignUp

def home(request):
    
    form = SignUpForm(request.POST or None)
    
    if form.is_valid():
        save_it = form.save(commit=False)
        save_it.save()
    
    return render_to_response("signup.html",
                              locals(),
                              context_instance=RequestContext(request))

def talks(request):
    talk_list = SignUp.talks.all()
    print talk_list
    extra_context = {"categories": talk_list}
    #return render_to_response("myapp/index.html", talk_list)
    return render_to_response("talks.html",
                              extra_context)
                              #locals(),
                              #context_instance=RequestContext(request))

def twittersignup(request):
      
    return render_to_response("twittersignup.html",
                              locals(),
                              context_instance=RequestContext(request))

def createtalk(request):

    validPasswordString = 'buzzkill'
    
    if request.method == 'POST': # If the form has been submitted...
        # ContactForm was defined in the the previous section
        form = SignUpForm(request.POST or None)
        if  not (form.data['Password'] == validPasswordString):
            print 'Try again'
            print
            return render_to_response("createtalk.html",
                              locals(),
                              context_instance=RequestContext(request))
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            
            save_it = form.save(commit=False)
            save_it.save()
            #return HttpResponseRedirect("create-talk-landing") # Redirect after POST
            return render_to_response("createtalklanding.html",
                              locals(),
                              context_instance=RequestContext(request))
        else:
            print "form was not valid"
    else:
        form = SignUpForm() # An unbound form
        
    return render_to_response("createtalk.html",
                              locals(),
                              context_instance=RequestContext(request))

def sampletalk(request):
    
  return render_to_response("sampletalk.html",
                              locals(),
                              context_instance=RequestContext(request))

def createtalklanding(request):
  print "im in here"
  return render_to_response("createtalklanding.html",
                              locals(),
                              context_instance=RequestContext(request))


