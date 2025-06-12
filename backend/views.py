from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Bienvenue sur SKMail 🎉</h1><p>Votre application fonctionne !</p>")
