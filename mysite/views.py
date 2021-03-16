from django.shortcuts import render

def HomeView(request):
    return render(request, 'mysite/main.html', context={'text':'Hello World'})

def LightbulbView(request):
    return render(request, 'mysite/lightbulbs.html', context={'text':'Hello World'})

def BlindsView(request):
    return render(request, 'mysite/blinds.html', context={'text':'Hello World'})

def TemperatureView(request):
    return render(request, 'mysite/temperature.html', context={'text':'Hello World'})
# Create your views here.
