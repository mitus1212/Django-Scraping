from time import sleep
from bs4 import BeautifulSoup
import math
from datetime import timedelta, timezone, datetime
import glob, os, os.path

from .models import Headline, UserProfile, Weather
from django.shortcuts import render, get_object_or_404, redirect

import shutil
import requests

from django.views.generic import (DeleteView)

from django.urls import reverse_lazy

# Create your views here.
requests.packages.urllib3.disable_warnings()

def news_list(request):
   
    weathers_info = Weather.objects.all()
    headlines = Headline.objects.all()

    url = "https://blockchain.info/ticker"
    
    json_data = requests.get(url).json()
    price = json_data['USD']['last']    

    context = {
        'object_list': headlines,
        'weather_in': weathers_info,
        'price': price,
    }  

    
    return render(request, "news/home.html", context)

def delete_article(request, id):
    
    item_to_delete = Headline.objects.filter(pk=id)
    if item_to_delete.exists():
        if request.user == item_to_delete[0].user:
            item_to_delete[0].delete()

    return redirect('/home/')
    


def scrape(request):

    filelist = glob.glob(os.path.join("/Users/Mateusz/Desktop/Django-Scraping-master/media/", "*.jpg"))
    try:
        for f in filelist:
            os.remove(f)
    except Exception:
        pass
    old_articles = Headline.objects.all()
    old_articles.delete()
 

    session = requests.Session()
    session.headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome"}
    url = 'https://www.onet.pl/'

    content = session.get(url, verify=False).content

    soup = BeautifulSoup(content, "html.parser")

    posts = soup.find_all('div', {'class': 'sectionLine'})
        
    for post in posts:
        try:
            title = post.find('span', {'class': 'title'}).get_text()
            link = post.find("a")['href']
            image_source = post.find('img')['src']
            image_source_solved = "https:{}".format(image_source)

                # stackoverflow solution

            media = '/Users/Mateusz/Desktop/Django-Scraping-master/media/'

            if not image_source_solved.startswith(("data:image", "javascript")):
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
                    shutil.move(current_image_absolute_path, media)
                    # end of stackoverflow solution

                new_headline = Headline()
                new_headline.title = title
                new_headline.url = link
                new_headline.image = local_filename
                new_headline.save()
                sleep(1)
                
                if Headline.objects.all().count() == 5:
            
                    return redirect('/home/')
        except:
            pass
    return redirect('/home/')


def scrape_weather(request):
    if request.method == 'POST':

        old_weather = Weather.objects.all()
        old_weather.delete()


        api_adress = "http://api.openweathermap.org/data/2.5/weather?q="
        api_key = "&appid=3a99cf24b53d85f4afad6cafe99d3a34"
        city = request.POST.get("city")
        
            
        url = api_adress + city + api_key
       
        if url == (api_adress + api_key):
            url = api_adress + "warsaw" + api_key
       
        json_data = requests.get(url).json()
        try:
            weather = json_data['weather'][0]['main']
            degree_kelvin = int(json_data['main']['temp'])
            degree = degree_kelvin-273
            pressure = json_data['main']['pressure']   
            new_weather = Weather()
            new_weather.city = city
            new_weather.degree = degree
            new_weather.pressure = pressure
            new_weather.weather = weather
            new_weather.save()   
        except:
            pass

        
    return redirect('/home/')


def weather_remove(request, pk):
 
    weather = get_object_or_404(Weather, pk=pk)
    weather.delete()

    return redirect('/home/')


def article_remove(request, pk):
  
    article = get_object_or_404(Headline, pk=pk)
    article.delete()
    
    return redirect('/home/')


