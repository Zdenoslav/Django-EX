from django.shortcuts import render

# Create your views here.
def article_list(request):
    return render(request,'articles/templates/articles/articles_list.html' )
