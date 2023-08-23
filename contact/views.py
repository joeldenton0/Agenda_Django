# from asyncio.windows_events import NULL
from django.shortcuts import render, redirect
from .models import Contact
from .forms import ContactForm
from django.contrib import messages

def index(request, letter= None):  # Vista para busqueda por letras o barra de busqueda.
    if letter != None:
        contacts = Contact.objects.filter(name__istartswith=letter)
    else:
        contacts = Contact.objects.filter(name__icontains=request.GET.get('search', ''))

    context = {
        'contacts' : contacts
    }

    return render(request, "contact/index.html", context)

def sorted_index(request, order):  #Vista para ordenar en forma ascendente o descendente.
    if order.startswith('-'):
        order_field = order[1:]
        contacts = Contact.objects.all().order_by('-' + order_field)
        current_order = '-' + order_field  # Agregar el signo menos al orden actual.
    else:
        order_field = order
        contacts = Contact.objects.all().order_by(order_field)
        current_order = order

    context = {
        'contacts': contacts,
        'current_order': current_order
    }

    return render(request, "contact/index.html", context)

def view(request, id):  # Vista para renderizar detalles de contacto.
    contact = Contact.objects.get(id=id)
    context = {
        'contact': contact
    }

    return render(request, "contact/detail.html", context)

def edit(request, id):  # Vista para editar datos de contacto.
    contact = Contact.objects.get(id=id)
    if request.method == 'GET':
        form = ContactForm(instance= contact)
        context = {
            'form' : form,
            'id' : id
        }

        return render(request, "contact/edit.html", context)

    if request.method == 'POST':
        form = ContactForm(request.POST, instance= contact)
        if form.is_valid():
            form.save()
            context = {
                'form' : form,
                'id' : id
            }
            messages.success(request, 'Contacto actualizado.')
            return render(request, "contact/edit.html", context)

def create(request):  # Vista para añadir nuevo contacto.
    if request.method == 'GET':
        form = ContactForm()
        context = {
            'form' : form
        }
        return render(request, "contact/create.html", context)

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact')

def delete(request, id):  # Vista para borrar contactos.
    del_contact = Contact.objects.get(id=id)
    if request.method == 'POST':
        del_contact.delete()
        return redirect('contact')
        
    return render(request, 'contact/delete_contact.html', {'id': id})