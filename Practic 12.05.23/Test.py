
import threading


def print_numbers():
    for i in range(1, 6):
        print(i)

# Создание потока
thread = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_numbers)

thread_list = [threading.Thread(target=print_numbers) for _ in range(10)]

for thread in thread_list:
    thread.start()
print(threading.enumerate())
# Запуск потока
# thread.start()
# thread2.start()
#
# # Ожидание завершения потока
# print(thread.is_alive())
# thread2.join()

print("Главный поток завершен")



import threading

counter = 0
counter_lock = threading.Lock()

def increment_counter():
    global counter
    with counter_lock:
        for _ in range(100000):
            counter += 1

# Создание потоков
threads = []
for _ in range(10):
    thread = threading.Thread(target=increment_counter)
    threads.append(thread)
    thread.start()

# Ожидание завершения всех потоков
for thread in threads:
    thread.join()

print("Значение счетчика:", counter)


import grequests

# Создаем список URL-адресов для запросов
urls = ['https://www.example.com', 'https://www.google.com', 'https://www.github.com']

# Создаем список объектов grequests.Request для каждого URL-адреса
requests = (grequests.get(url) for url in urls)

# Отправляем запросы асинхронно
responses = grequests.map(requests)

# Обрабатываем результаты запросов
for response in responses:
    if response is not None:
        print("Response:", response.url, response.status_code)
    else:
        print("Request failed")