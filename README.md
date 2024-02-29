<html>
<h1>SDK для <a href='https://my.digiseller.com'>Digiseller</a></h1>
<p>Данная библиотека написана для удобного и быстрого взаимодействия с API сервиса <a href='https://my.digiseller.com'>Digiseller</a>.<br>
Чтобы использовать эту библиотеку, необходимо получить <a href='https://my.digiseller.com/inside/api_keys.asp'>API ключ</a> и ID продавца.</p>

<h2>Начало работы (создание Client):</h2>
<ol>
	<li>
		Поместите папку digiseller в корень проекта
	</li>
	<li>
		Установите необходимые зависимости<br>
		<code>pip install -r digiseller/requirements.txt</code>
	</li>
	<li>
		Импортируйте класс клиента из библиотеки<br>
		<code>from digiseller import Client</code>
	</li>
	<li>
		Создайте объект клиента, передав в него API ключ и ID продавца<br>
		<code>client = Client(API_KEY, SELLER_ID)</code>
	</li>
</ol>

<h3>Функции объекта класса Client:</h3>

Проверка уникального кода<br>
<code>check_code = client.check_code(code)</code><br>
<i>code - Уникальный код покупки</i>

Получение списка диалогов<br>
<code>messages = client.get_dialogs()</code>

Отправка сообщения<br>
<code>message = client.send_message(invoice_id, message)</code><br>
<i>invoice_id - Номер заказа<br>
message - Текст сообщения</i>

<p>Для работы с конкретным заказом можно создать объект класса Invoice<p>

<h2>Создание Invoice</h2>

<code>from digiseller import Invoice
invoice = Invoice(client, invoice_id)</code><br>
<i>client - объект класса Client<br>
invoice_id - номер заказа</i><br>

<h3>Параметры объекта:</h3>
client - объект класса Client<br>
invoice_id - ID(номер) заказа<br>
json - json ответ на запрос<br>
good_id - ID товара<br>
amount - Сумма зачисленная на счет<br>
purchase_date - Дата и время платежа<br>
count_goods - Количество единиц товара<br>
unique_code - Статус уникального кода<br>

<h3>Функции объекта класса Invoice:</h3>
<oi>
	<li>
		Получение всех сообщений из диалога заказа<br>
		<code>invoice.get_all_messages()</code>
	</li>
	<li>
		Отправка сообщения (дублирует функцию из Client)<br>
		<code>invoice.send_message(message)</code><br>
		<i>message - Текст сообщения</i> 
	</li>
	<li>
		Удаление сообщения из диалога<br>
		<code>invoice.delete_message(message_id)</code><br>
		<i>message_id - ID сообщения</i> 
	</li>
	<li>
		Установить флаг "прочитано"<br>
		<code>invoice.set_read()</code> 
	</li>
</oi>
