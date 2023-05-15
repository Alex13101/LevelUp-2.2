from selenium import webdriver

from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By

# Создание экземпляра драйвера

driver = webdriver.Chrome()

# Переход на страницу Google

driver.get("https://www.google.com")

# Найти поле ввода поискового запроса и ввести запрос

search_box = driver.find_element(By.ID, 'APjFqb')

search_box.send_keys("python selenium")

search_box.send_keys(Keys.RETURN)

# Дождаться загрузки результатов поиска

driver.implicitly_wait(3)

# Получить результаты поиска

search_results = driver.find_elements(By.CLASS_NAME, 'MjjYud')

# Вывести заголовки результатов поиска

for result in search_results:
    #     title = result.find_element(By.CLASS_NAME, 'LC20lb MBeuO DKV0Md')

    print(result)

html = driver.page_source

with open('google.html', 'w', encoding='utf-8') as f:
    f.write(html)

# Закрыть браузер

driver.quit()
