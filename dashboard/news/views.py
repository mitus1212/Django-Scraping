from time import sleep
from bs4 import BeautifulSoup
import math
from datetime import timedelta, timezone, datetime
import os
from .models import Headline, UserProfile, Weather
from django.shortcuts import render, get_object_or_404, redirect

import shutil
import requests

from django.views.generic import (DeleteView)

from django.urls import reverse_lazy

# Create your views here.
requests.packages.urllib3.disable_warnings()

def news_list(request):
    user_prof = UserProfile.objects.filter(user=request.user).first()
    now = datetime.now(timezone.utc)
    time_difference = now - user_prof.last_scrape
    time_difference_in_hours = time_difference / timedelta(minutes=60)
    next_scrape = 24 - time_difference_in_hours

    if time_difference_in_hours <= 24:
        hide_me = True
    else:
        hide_me = False

    weathers_info = Weather.objects.all()

    headlines = Headline.objects.all()
    context = {
        'object_list': headlines,
        'hide_me': hide_me,
        'next_scrape': math.ceil(next_scrape),
        'weather_in': weathers_info,
    }  

    
    return render(request, "news/home.html", context)

def delete_article(request, id):
    item_to_delete = Headline.objects.filter(pk=id)
    if item_to_delete.exists():
        if request.user == item_to_delete[0].user:
            item_to_delete[0].delete()
    return redirect('/home/')
    


def scrape(request):
    old_articles = Weather.objects.all()
    old_articles.delete()
    user_prof = UserProfile.objects.filter(user=request.user).first()
    if user_prof is not None:
        user_prof.last_scrape = datetime.now(timezone.utc)
        user_prof.save()

    session = requests.Session()
    session.headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"}
    url = 'https://www.onet.pl/'

    content = session.get(url, verify=False).content

    soup = BeautifulSoup(content, "html.parser")

    #posts = soup.find_all('a',{'class':'itemBox itemBox_3_1 s1_155'})

    posts = soup.find_all('div', {'class': 'sectionLine'})
        
    for post in posts:
        title = post.find('span', {'class': 'title'}).get_text()
        link = post.find("a")['href']
        image_source = post.find('img')['src']
        image_source_solved = "http:{}".format(image_source)

            # stackoverflow solution

        media_root = '/Users/mat/Desktop/jspython/just django/dashboard/media_root'
        if not image_source_solved.startswith(("data:image", "javascript")):
            #exists = os.path.isfile(media_root+image_source_solved)
            exists = 1
            if exists == 2:
                pass
            else:
                local_filename = image_source_solved.split('/')[-1].split("?")[0]+".jpg"
                r = session.get(image_source_solved, stream=True, verify=False)
                with open(local_filename, 'wb') as f:
                    for chunk in r.iter_content(chunk_size=1024):
                        f.write(chunk)

                current_image_absolute_path = os.path.abspath(local_filename)
                shutil.move(current_image_absolute_path, media_root)

                # end of stackoverflow solution

            new_headline = Headline()
            new_headline.title = title
            new_headline.url = link
            new_headline.image = local_filename
            new_headline.save()
            sleep(1)




    return redirect('/home/')


def scrape_weather(request):
    if request.method == 'POST':

        old_weather = Weather.objects.all()
        old_weather.delete()
        api_adress = "http://api.openweathermap.org/data/2.5/weather?q="
        api_key = "&appid=3a99cf24b53d85f4afad6cafe99d3a34"
        city = request.POST.get("city")
        
        url = api_adress + city + api_key

        json_data = requests.get(url).json()
        new_weather = json_data['weather'][0]['main']
        degree_kelvin = int(json_data['main']['temp'])
        degree = degree_kelvin-273
        pressure = json_data['main']['pressure']      
        
        new_weather = Weather()
        new_weather.degree = degree
        new_weather.pressure = pressure
            
        new_weather.weather = new_weather
        new_weather.save()
        
    return render(request, "news/home.html")

        

def weather_remove(request, pk):
    weather = get_object_or_404(Weather, pk=pk)
    weather.delete()
    return redirect('/home/')


def article_remove(request, pk):
    article = get_object_or_404(Headline, pk=pk)
    article.delete()
    return redirect('/home/')


