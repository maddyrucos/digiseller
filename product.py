import requests

def get_json(client, product_id):
	token = client.get_token()

	url = f'https://api.digiseller.ru/api/products/options/list/{product_id}'

	headers = {"Accept":"application/json"}

	params = {
		"token": token
	}

	r = requests.get(url=url, params=params, headers=headers)

	return r.json()

# Класс товаров. Для создания объекта необходимо передать объект клиента и номер товара
class Product:

	def __init__(self, client, product_id):
		self.client = client
		self.product_id = product_id
		self.json = get_json(client, product_id)
