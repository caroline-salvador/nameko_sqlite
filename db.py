import sqlite3
import os

from datetime import datetime

database = "./database.db"
		
def create_database():
	if os.path.exists(database):
		return
	
	try:
		connection = sqlite3.connect(database)
		cursor = connection.cursor()
		
		cursor.execute('''CREATE TABLE IF NOT EXISTS weather(
			id integer PRIMARY KEY,
			city text NOT NULL, 
			country text NOT NULL, 
			temp_now text NOT NULL,
			temp_min text NOT NULL, 
			temp_max text NOT NULL,
			time text NOT NULL,
			sunrise text NOT NULL,
			sunset text NOT NULL,
			read_date date NOT NULL)''')

		connection.commit()
		close_db(connection)
		print("Tabela weather criada com sucesso")
	
	except Exception as error:
		print(str(error))

	return
	
def insert_table(dict_weather):
	try:
		connection = sqlite3.connect(database)
		cursor = connection.cursor()
		
		read_date = datetime.now().date().strftime('%Y-%m-%d')
		
		result = select_table(cursor)
		insert = True
		
		if result:
			for row in result:
				if row[1] == dict_weather['city'] and row[2] == dict_weather['country'] and row[9] == read_date:
					
					print("Previsão para o dia {0} - {1}/{2} já está armazenada no banco de dados". \
						format(read_date, dict_weather['city'], dict_weather['country']))
					
					insert = False
					break
		
		if insert:
			sql = "INSERT INTO weather(city, country, temp_now, temp_min, temp_max, time, sunrise, sunset, read_date) \
				VALUES('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}', '{7}', '{8}');". \
				format(dict_weather['city'], 
					   dict_weather['country'], 
					   dict_weather['temp_now'],
					   dict_weather['temp_min'], 
					   dict_weather['temp_max'],
					   dict_weather['time'],
					   dict_weather['sunrise'],
					   dict_weather['sunset'],
					   read_date)
				
			cursor.execute(sql)
			connection.commit()
			
	except Exception as error:
		print(str(error))
		connection.rollback()
		
	finally:	
		close_db(connection)
	
	return
	
def select_table(cursor):
	result = cursor.execute("SELECT * FROM weather")
	result = cursor.fetchall()
	
	# Somente para visualizar os registros da tabela
	for member in result:
		print(member)

	return result
	
def close_db(connection):
	if connection:
		connection.close()
		print("Conexão fechada.")
	
	return






















