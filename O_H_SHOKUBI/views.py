from django.shortcuts import render, redirect
from django.core.paginator import Paginator


from . import models
# from models import News

# Create your views here.
def home(request):
    latest_news = models.News.objects.all().order_by('-created_time_date')[:3]
    return render(request, 'index1.html',{'all_news':latest_news})

def news(request):
    all_news = models.News.objects.all().order_by('-created_time_date')
    
    # Create paginator — 9 news per page
    paginator = Paginator(all_news, 9)
    
    # Get current page number from URL
    page_number = request.GET.get('page')
    
    # Get page object
    page_obj = paginator.get_page(page_number)
    
    return render(request,'news.html', {'page_obj':page_obj})

def news_create(request):
    if request.user.is_authenticated and request.user.is_superuser:
        if request.method == 'POST':
            headline = request.POST.get('headline')
            news_images = request.POST.get('news_images')
            news_body = request.POST.get('news_body')
            
            new_news = models.News.objects.create(
                headline = headline,
                news_images = news_images,
                news_body = news_body
            )
            new_news.save()
        return render(request, 'news_create.html')
    return redirect('news')

def news_edit(request, headline_for_url):
    return render(request, 'news_edit.html')

def news_detail(request, headline_for_url):
    news_model = models.News.objects.get(headline_for_url=headline_for_url)
    print(news_model.news_images)
    return render(request,'news_detail.html', {'news':news_model})

def people(request):
    lawyers = models.Lawyer.objects.all()
    
    paginator = Paginator(lawyers, 9)
    
    # Get current page number from URL
    page_number = request.GET.get('page')
    
    # Get page object
    page_obj = paginator.get_page(page_number)
    return render(request, 'people.html', {'page_obj':page_obj})

def people_info(request, name_for_url):
    lawyers = models.Lawyer.objects.get(name_for_url=name_for_url)
    return render(request, 'people_info.html', {'lawyer':lawyers})

def base(request):
    return render(request, 'base.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def careers(request):
    return render(request, 'careers.html')

def practices(request):
    practice_area = models.Practice.objects.all()
    return render(request, 'practices.html', {'practice_area':practice_area})

def practices_info(request, practice_name_for_url):
    practice_area = models.Practice.objects.get(practice_name_for_url=practice_name_for_url)
    practice_lawyers = practice_area.lawyers.all()
    return render(request, 'practices_info.html', {'practice_lawyers':practice_lawyers, 'practice_area':practice_area})

# from django.contrib.auth.models import User
# from django.http import JsonResponse

# def debug_users(request):
#     if not request.user.is_superuser:
#         return JsonResponse({"error": "forbidden"}, status=403)

#     users = list(User.objects.values("username", "email", "is_superuser", "is_staff"))
#     return JsonResponse(users, safe=False)
