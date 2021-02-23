from django.shortcuts import render

def LightbulbView(request):
    return render(request, 'mysite/index.html', context={'text':'Hello World'})
# Create your views here.
