from django.http import HttpResponse

def helloworldfunction(request):
    returnedobject = HttpResponse('<h1>hello world</h1>')
    return returnedobject