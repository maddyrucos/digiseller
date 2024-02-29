from client import Client
import requests



# Получить JSON с информацией о заказе
def get_json(client, invoice_id):
	token = client.get_token()
	url=(f'https://api.digiseller.ru/api/purchase/info/{invoice_id}')

	params = {
        "invoice_id": invoice_id,
        "token": token,
    }

	headers = {'Accept': 'application/json'}

	r = requests.get(url, params=params, headers=headers)
	res = r.json()

	return res



# Класс заказа. Для создания объекта необходимо передать объект клиента и номер заказа
class Invoice:
	
	def __init__(self, client: Client, invoice_id: int):
		self.client = client
		self.invoice_id = invoice_id
		self.json = get_json(self.client, self.invoice_id)
		self.product_id = self.json['content']['item_id'] # ID товара
		self.product_name = self.json['content']['name'] # Название товара
		self.amount = self.json['content']['amount'] # Сумма зачисленная на счет
		self.purchase_date = self.json['content']['purchase_date'] # Дата и время платежа
		self.count_goods = self.json['content']['cnt_goods'] # Количество единиц товара
		self.unique_code = self.json['content']['unique_code_state'] #Статус уникального кода
		# Список будет расширяться


	def get_token(self):
		return self.client.get_token()


	# Все сообщения заказа
	def get_all_messages(self):
		token = self.get_token()
		url = f'https://api.digiseller.ru/api/debates/v2'

		params = {
	        "token": token,
	        "id_i": self.invoice_id,
	    }

		headers = {'Accept': 'application/json'}

		r = requests.get(url, params=params, headers=headers)
		res = r.json()

		return res


	# Отправка сообщения в заказ (диалог)
	def send_message(self, message: str):
		self.client.send_message(self.invoice_id, message)


	# Отправка файлов в заказ (диалог)
	def send_file(self, message: str, file):
		self.client.send_file(self.invoice_id, message, file)


	# Удаление сообщения
	def delete_message(self, message_id):
		token = self.get_token()
		url = f'https://api.digiseller.ru/api/debates/v2/{message_id}'

		headers = {'Accept': 'application/json'}

		params = {
			"token": token,
	        "id_i": self.invoice_id,
	        "id": message_id
		}

		res = requests.delete(url=url, headers=headers, params=params)

		return res


	# Установка флага "прочитано"
	def set_read(self):
		token = self.get_token()
		url = f'https://api.digiseller.ru/api/debates/v2/seen'

		headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}

		params = {
			"token": token,
	        "id_i": self.invoice_id,
		}

		res = requests.post(url=url, headers=headers, params=params)

		return res