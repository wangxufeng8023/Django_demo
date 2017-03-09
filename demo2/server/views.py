from django.template import loader,Context,Template
from django.http import HttpResponse
from django.shortcuts import render_to_response
#def index(req):
    
    #t = loader.get_template('index.html')
  
    #c = Context({'uname':'alen'})
  
    #html = t.render(c)
    #return HttpResponse(html)
#def index(req):
    
    #t = Template('<h1>hello {{uname}}</h1>')
    #c = Context({'uname':'lili'})
    #return HttpResponse(t.render(c))
def index2(req):
   return render_to_response('index.html',{'uname':'jiajia'})