import pyowm
from nameko.rpc import rpc, RpcProxy

from db import insert_table

class Weather(object):
	name="weather"
	
	@rpc
	def consult_weather(self, dict_info):
		key = 'eb8b1a9405e659b2ffc78f0a520b1a46'
		local = "{0}, {1}".format(dict_info["city"].lower(), dict_info["country"].lower())
		dict_result = None
		obs = None
		
		try:
			owm = pyowm.OWM(key, language='pt')
			obs = owm.weather_at_place(local)
		except Exception as error:
			print(str(error))

		if obs:		
			data_weather = obs.get_weather()

			dict_result = {
				'temp_now': data_weather.get_temperature(unit='celsius')['temp'],
				'temp_max': data_weather.get_temperature(unit='celsius')['temp_max'],
				'temp_min': data_weather.get_temperature(unit='celsius')['temp_min'],
				'time': data_weather.get_reference_time(timeformat='date').time().strftime("%H:%M:%S"),
				'sunrise': data_weather.get_sunrise_time('date').time().strftime("%H:%M:%S"),
				'sunset': data_weather.get_sunset_time('date').time().strftime("%H:%M:%S")
			}
			
		return dict_result

class Consult(object):
	name="consult"
	weather_api = RpcProxy("weather")
	
	@rpc
	def get_weather(self, dict_info):
		result = self.weather_api.consult_weather.call_async(dict_info)
		
		if result.result():
			dict_result = result.result()
			dict_result['city'] = dict_info["city"].lower()
			dict_result['country'] = dict_info["country"].lower()
	
			insert_table(dict_result)
	
		return result.result()
		
		