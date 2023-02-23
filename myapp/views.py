from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'index.html')


def counter(request):
    text = request.POST['text'] # 'text' variable comes from -> index.html -> textarea -> name
    context = {
        'text': text,
        'wordCount': len(text.split())
    }
    return render(request, 'counter.html', context)
