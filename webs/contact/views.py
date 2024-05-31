from django.shortcuts import render

# Create your views here.
def contact(request):
    context={
        'name':'contact',
    } 
    return render(request,'contat/contact.html',context)