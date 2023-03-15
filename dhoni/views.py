from django.shortcuts import render

# Create your views here.
def jinja_second(request):
    d={'name':'Naveen','mobileNo':7815872910}
    return render(request,'jinja_second.html',context=d)