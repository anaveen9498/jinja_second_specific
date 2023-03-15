from django.shortcuts import render

# Create your views here.
def jinja_second(request):
    d={'name':'naveenaveen'}
    return render(request,'jinja_second.html',context=d)