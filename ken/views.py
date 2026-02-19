from django.shortcuts import render

# Create your views here.
def contact(request):
    return render(request, 'contact.html')
def index(request):
    return render(request, 'index.html')
def venue(request):
    return render(request, 'venue.html')
def privacy(request):
    return render(request, 'privacy.html')
def terms(request):
    return render(request, 'terms.html')
def home(request):
    return render(request, 'home.html')
def starter_page(request):
    return render(request, 'starter_page.html')
def buy_tickets(request):
    return render(request, 'buy_tickets.html')
def speakers_details(request):
    return render(request, 'speakers_details.html')

