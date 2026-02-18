from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello World! This is running on AWS.")
