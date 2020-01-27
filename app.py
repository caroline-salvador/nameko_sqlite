from flask import Flask, jsonify
from nameko.standalone.rpc import ClusterRpcProxy

from db import create_database

app_service = Flask('app_service')
CONFIG = {'AMQP_URI': 'amqp://guest:guest@localhost'}

@app_service.route('/<string:city>/<string:country>')
def index(city, country):	
	with ClusterRpcProxy(CONFIG) as rpc:    		
	
		result = rpc.consult.get_weather.call_async({"city": city.lower(), "country": country.lower()})
		dict_weather = result.result()
		
		if not dict_weather:
			return jsonify(Estado_Tarefa="Verifique se a URL está correta: {0} - {1}".format(city, country))
	
		return jsonify(Cidade=city.lower(), 
					   País=country.lower(),
					   Hora_Medição=dict_weather['time'],
					   Temperatura_Atual=dict_weather['temp_now'],
					   Temperatura_Máxima=dict_weather['temp_max'],
					   Temperatura_Mínima=dict_weather['temp_min'],
					   Nascer_Sol=dict_weather['sunrise'],
					   Por_Sol=dict_weather['sunset'])
		
if __name__ == "__main__":	
	try:		
		create_database()
		app_service.run(port=8000)
	except Exception as error:
		print(str(error))
	

