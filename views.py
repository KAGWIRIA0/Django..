from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')

def services(request):
    our_services= ["Dinner", "Free Breakfast"," Free Parking", "Bonfires"]
    price = 10000
    date ='22-11-2024'
    return render(request,'services.html',
                  {"services":our_services, "price":price, "date":date})

def about(request):
    return render(request, 'about.html')

#display data
#loops
#if statements
#Templating Engine Language