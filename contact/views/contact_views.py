from django.shortcuts import render,get_object_or_404,redirect
from contact import models
from django.db.models import Q
from django.core.paginator import Paginator
# Create your views here.

def index(request):
    contacts = models.Contact.objects.filter(show=True).order_by('-id')
    paginator = Paginator(contacts, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'site_title': 'Contatos - ',
    }
    return render(request, 'contact/index.html', context)




def contact(request, contact_id):
    # contact = models.Contact.objects.filter(pk=contact_id).first()
    contact = get_object_or_404(models.Contact, pk=contact_id, show=True)
    site_title = f'{contact.first_name} {contact.last_name} - '
    context = {
        'contact':contact,
        'site_title':site_title,
    }
    return render(request, 'contact/contact.html', context)







def search(request):
    search_value = request.GET.get('q', '').strip()
    if search_value == '':
        return redirect('contact:index')
    
    contacts = models.Contact.objects.filter(show=True)\
        .filter(Q(first_name__icontains=search_value) |
                Q(last_name__icontains=search_value) |
                Q(phone__icontains=search_value) |
                Q(email__icontains=search_value) 
        ).order_by('-id')

    paginator = Paginator(contacts, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'site_title' : 'Search -'
    }
    
    return render(request, 'contact/index.html', context)