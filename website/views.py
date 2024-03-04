from django.shortcuts import render, redirect
from django.contrib import messages

from website_admin.models import About_executive_team, About_executive_team2, About_functional_team, About_technical_team1, About_technical_team2, Message, News, Service

# Create your views here.

def home(request):
    return render(request, "index.html")

def service(request):
    services = Service.objects.all()
    context = {
        "services": services
    }
    return render(request, "service.html", context)

def aboutUs(request):
    about = About_executive_team.objects.all()
    about2 = About_functional_team.objects.all()
    about3 = About_technical_team1.objects.all()
    about4 = About_technical_team2.objects.all()
    about5 = About_executive_team2.objects.all()
    context = {
        "about": about,
        "about2": about2,
        "about3": about3,
        "about4": about4,
        "about5": about5,
    }
    return render(request, "aboutUs.html", context)

def contact(request):
    print(request.method)
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        if Message.objects.filter(email=email).exists():
            messages.error(request, 'Email already exist')
            return render(request, "contact.html")
    

        if not name or not email or not subject or not message:
            messages.warning(request, "Please fill in all fields")
            return render(request, "contact.html")

        try:
            contact_message = Message.objects.create(email=email, name=name, subject=subject, message=message)
            contact_message.save()
            messages.success(request, "Message sent successfully")
            return redirect('contact')
        except:
          messages.error(request, "Error sending message")
          return render(request, "contact.html")
    else:
        return render(request, "contact.html")

def case(request):
    return render(request, "case.html")

def news(request):
    news = News.objects.all()
    context = {
         "news": news
    }
    return render(request, "news.html", context)
