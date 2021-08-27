from django.shortcuts import render
from .models import About, Contact_form, Contact


# Create your views here
def homepage(request):
    return render(request, "home.html")


def about(request):
    about_data = About.objects.all()
    context = {
        'about_data': about_data
    }

    return render(request, 'about.html', context)


def contact(request):
    contact_data = Contact.objects.all()
    ary = {
        'contact_data': contact_data
    }
    if request.method == "POST":
        fullname = request.POST.get("Name")
        email = request.POST.get("email")
        suggestion = request.POST.get("Comment")

        person = Contact_form(full_name=fullname, email=email, suggestion=suggestion)
        person.save()

    return render(request, "contact.html", ary)
