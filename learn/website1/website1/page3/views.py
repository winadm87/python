from django.shortcuts import render

# Create your views here.
def index(request):
    context = {'github_url': 'https://github.com',
               'page_with_pictures': 'http://127.0.0.1:8000/page2',
               }
    return render(request, 'webpage3/index.html', context)