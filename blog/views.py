from django.shortcuts import render

# Create your views here.
def publicacion_lista(request):
    return render(request, 'blog/publicacion_lista.html', {})
