import hashlib
import requests
import time



class Client:


	def __init__(self, api_key: str, seller_id: int):
		self.api_key = api_key
		self.seller_id = seller_id



	# Получение уникального токена для взаимодействия с API
	def get_token(self): 
		timestamp = int(time.time())
		data = self.api_key + str(timestamp)
		sign = hashlib.sha256(data.encode('utf-8')).hexdigest()
	    
		json = {
	        "seller_id": self.seller_id,
	        "timestamp": timestamp,
	        "sign": sign,
	    }

		url = 'https://api.digiseller.ru/api/apilogin'
		headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
		r = requests.post(url, json=json, headers=headers)
	    
		if r.status_code != 200:
			return None
		res = r.json()
	    
		if res['retval'] != 0:
			return None
	    
		return res['token']


	# Проверка уникального кода
	def check_code(self, code):
		token = self.get_token()
		url= f'https://api.digiseller.ru/api/purchases/unique-code/{code}'

		params = {
	        "unique_code": code,
	        "token": token
	    }

		headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}

		r = requests.get(url, params=params, headers=headers)
		res = r.json()

		return res


	# Получение списка диалогов
	def get_dialogs(self):
		token = self.get_token()
		url= 'https://api.digiseller.ru/api/debates/v2/chats'

		params = {
	        "token": token
	    }

		headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}

		r = requests.get(url,  params=params,  headers=headers)
		res = r.json()

		return res


	# Отправка сообщения
	def send_message(self, invoice_id, message):
		token = self.get_token()
		url = 'https://api.digiseller.ru/api/debates/v2'

		json = {
	        'message' : message
	    }
		params = {
	        "token": token,
	        "id_i" : invoice_id,
	    }

		headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}

		r = requests.post(url, params=params, headers=headers, json=json)
		res = r.status_code

		return res


	# Отправка сообщения c файлом
	def send_files(self, invoice_id, message, files):
	    token = self.get_token()
	    url = 'https://api.digiseller.ru/api/debates/v2'

	    json = {
	        "message": message,
	        "files": files,
	    }
	    
	    params = {
	        "token": token,
	        "id_i" : invoice_id,
	    }

	    headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}

	    r = requests.post(url, params=params, headers=headers, json=json)
	    res = r.status_code

	    return res