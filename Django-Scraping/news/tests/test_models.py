from django.test import TestCase

from .models import Weather, Headline

# Create your tests here.

class WeatherModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Weather.objects.create(weather="sunny",degree="25",pressure="1024")
    
    def test_weather_label(self):
        weather_model_test = Weather.objects.get(id=1)
        field_label = weather_model_test._meta.get_field('weather').verbose_name
        self.assertEquals(field_label, 'weather')

    def test_pressure_label(self):
        weather_model_test = Weather.objects.get(id=1)
        field_label = weather_model_test._meta.get_field('pressure').verbose_name
        self.assertEquals(field_label, 'pressure')

    def test_degree_label(self):
            weather_model_test = Weather.objects.get(id=1)
            field_label = weather_model_test._meta.get_field('degree').verbose_name
            self.assertEquals(field_label, 'degree')

class HeadlineModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Headline.objects.create(title="headline",url="https://www.facebook.com/")
    
    def test_title_label(self):
        headline = Headline.objects.get(id=1)
        field_label = headline._meta.get_field('title').verbose_name
        self.assertEquals(field_label,'title')

    def test_url_label(self):
        headline = Headline.objects.get(id=1)
        field_label = headline._meta.get_field('url').verbose_name
        self.assertEquals(field_label,'url')

    def test__str__(self):
        headline = Headline.objects.get(id=1)
        self.assertEquals(headline.__str__(),title)




