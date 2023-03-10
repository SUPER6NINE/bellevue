import requests
from pprint import pprint
def weather_data(query):
	res=requests.get('http://api.openweathermap.org/data/2.5/weather?'+query+'&APPID=bbeeeb23fe7028f4b06f5b53f5519cbb&units=imperial');
	return res.json();
def print_weather(result,city):
	print("{}'s temperature: {}°F ".format(city,result['main']['temp']))
	print("Wind speed: {} f/s".format(result['wind']['speed']))
	print("Description: {}".format(result['weather'][0]['description']))
	print("Weather: {}".format(result['weather'][0]['main']))
def main():
	city=input('Enter the city:')
	print()
	try:
	  query='q='+city;
	  w_data=weather_data(query);
	  print_weather(w_data, city)
	  print()
	except:
	  print('City name not found...')
if __name__=='__main__':
	main()