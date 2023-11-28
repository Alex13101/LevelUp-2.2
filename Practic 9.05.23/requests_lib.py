import requests

'''Метод GET: используется для получения информации с сервера. Пример:'''


response = requests.get('https://www.mail.ru')

print(response.text)


'''Метод POST: используется для отправки данных на сервер, 
например, для создания нового ресурса. Пример:'''

data = {'username': 'user', 'password': 'pass'}
response = requests.post('https://www.mail.ru/login', data=data)
print(response.status_code)

'''Метод PUT: используется для обновления существующего 
ресурса на сервере. Пример'''

data = {'name': 'new name', 'age': 25}
response = requests.put('https://www.mail.ru/profile', data=data)
print(response.status_code)


'''Метод DELETE: используется для удаления ресурса на сервере. Пример:'''


response = requests.delete('https://www.mail.ru/item/1')
print(response.status_code)


'''Параметр params: используется для передачи параметров в запросе. Пример:'''


payload = {'key1': 'value1', 'key2': 'value2'}
response = requests.get('https://www.mail.ru/get', params=payload)
print(response.url)


'''Параметр headers: используется для отправки заголовков в запросе. Пример:'''


headers = {'User-Agent': 'Mozilla/5.0'}
response = requests.get('https://www.mail.ru', headers=headers)
print(response.status_code)



'''Параметр cookies: используется для передачи cookie в запросе. Пример:'''


cookies = {'session_id': '123'}
response = requests.get('https://www.example.com', cookies=cookies)
print(response.status_code)


'''Параметр timeout: используется для установки времени ожидания ответа от сервера. Пример:'''


response = requests.get('https://www.mail.ru', timeout=5)
print(response.status_code)


'''Атрибут content возвращает содержимое ответа в виде байтов. 
Этот атрибут полезен, когда необходимо получить содержимое в бинарном формате, 
например, для сохранения в файл или передачи по сети. Например, чтобы получить 
содержимое в виде байтов, можно использовать следующий код:'''


'''response = requests.get('https://www.mail.ru')
content = response.content
print(content)'''


'''Важно помнить, что использование атрибута content может потребовать дополнительной обработки, 
например, если содержимое ответа является изображением или другим бинарным файлом. 
В таком случае необходимо сохранить содержимое в файл или передать его в 
соответствующий обработчик.'''