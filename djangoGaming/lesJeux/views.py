from django.http import HttpResponse

def home(request):
  return HttpResponse('bonjour à tous et bienvenue sur django gaming !')