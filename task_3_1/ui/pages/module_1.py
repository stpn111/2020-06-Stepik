from selenium.webdriver.common.by import By
from ui.pages.module_base import ModuleBase
import time
import math


link_task1 = "http://suninjuly.github.io/simple_form_find_task.html"
link_task2 = 'http://suninjuly.github.io/find_link_text'
link_task3 = 'http://suninjuly.github.io/huge_form.html'
link_task4 = 'http://suninjuly.github.io/find_xpath_form'


class ModuleOne(ModuleBase):

    def task1_6_1(self):
        browser = self.driver()

        try:
            browser.get(link_task1)
            input1 = browser.find_element_by_tag_name('input')
            input1.send_keys("Ivan")
            input2 = browser.find_element_by_name('last_name')
            input2.send_keys("Petrov")
            input3 = browser.find_element_by_class_name('city')
            input3.send_keys("Smolensk")
            input4 = browser.find_element_by_id('country')
            input4.send_keys("Russia")
            button = browser.find_element_by_css_selector("button.btn")
            button.click()
        finally:
            browser.quit()

    def task_1_6_2(self):
        browser = self.driver()
        try:
            browser.get(link_task2)
            linked = browser.find_element_by_partial_link_text('224592')
            linked.click()

            input1 = browser.find_element_by_tag_name('input')
            input1.send_keys("Ivan")
            input2 = browser.find_element_by_name('last_name')
            input2.send_keys("Petrov")
            input3 = browser.find_element_by_class_name('city')
            input3.send_keys("Smolensk")
            input4 = browser.find_element_by_id('country')
            input4.send_keys("Russia")
            button = browser.find_element_by_css_selector("button.btn")
            button.click()
        finally:
            time.sleep(10)
            browser.quit()

    def task_1_6_3(self):
        browser = self.driver()
        try:
            browser.get(link_task3)
            elements = browser.find_elements_by_tag_name('input')
            for element in elements:
                element.send_keys("Мой ответ")

            button = browser.find_element_by_css_selector("button.btn")
            button.click()

        finally:
            # успеваем скопировать код за 30 секунд
            time.sleep(30)
            # закрываем браузер после всех манипуляций
            browser.quit()
            # не забываем оставить пустую строку в конце файла

    def task_1_6_4(self):
        browser = self.driver()
        try:
            browser.get(link_task4)
            elements = browser.find_elements_by_tag_name('input')
            for element in elements:
                element.send_keys("Мой ответ")

            button = browser.find_element(By.XPATH, '//button[contains(text(), "Submit")]')
            button.click()

        finally:
            # успеваем скопировать код за 30 секунд
            time.sleep(30)
            # закрываем браузер после всех манипуляций
            browser.quit()
            # не забываем оставить пустую строку в конце файла

    def task_1_6_5(self):
        driver_browser = self.driver()
        try:
            link1 = "http://suninjuly.github.io/registration1.html"
            link2 = "http://suninjuly.github.io/registration2.html"

            # при необходимости поменять на link1
            driver_browser.get(link2)

            # Ваш код, который заполняет обязательные поля
            input1 = driver_browser.find_element_by_tag_name('input')
            input1.send_keys("Ivan")
            input2 = driver_browser.find_element(By.XPATH, '//div[label[contains(., "Last name*")]]/input')
            input2.send_keys("Petrov")
            input3 = driver_browser.find_element(By.XPATH, '//div[label[contains(., "Email*")]]/input')
            input3.send_keys("test@mail.ru")
            button = driver_browser.find_element_by_css_selector("button.btn")
            button.click()

            # Проверяем, что смогли зарегистрироваться
            # ждем загрузки страницы
            time.sleep(1)

            # находим элемент, содержащий текст
            welcome_text_elt = driver_browser.find_element_by_tag_name("h1")
            # записываем в переменную welcome_text текст из элемента welcome_text_elt
            welcome_text = welcome_text_elt.text

            # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
            assert "Congratulations! You have successfully registered!" == welcome_text

        finally:
            # ожидание чтобы визуально оценить результаты прохождения скрипта
            time.sleep(10)
            # закрываем браузер после всех манипуляций
            driver_browser.quit()

    def task_1_part11(self):
        browser = self.driver()
        try:
            link = "http://suninjuly.github.io/registration1.html"
            browser.get(link)

            # Ваш код, который заполняет обязательные поля
            elements = browser.find_elements_by_css_selector(".first_block input")
            for element in elements:
                element.send_keys("xd")

            # Отправляем заполненную форму
            button = browser.find_element_by_css_selector("button.btn")
            button.click()

            # Проверяем, что смогли зарегистрироваться
            # ждем загрузки страницы
            time.sleep(1)

            # находим элемент, содержащий текст
            welcome_text_elt = browser.find_element_by_tag_name("h1")
            # записываем в переменную welcome_text текст из элемента welcome_text_elt
            welcome_text = welcome_text_elt.text

            # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
            assert "Congratulations! You have successfully registered!" == welcome_text

        finally:
            # ожидание чтобы визуально оценить результаты прохождения скрипта
            time.sleep(5)
            # закрываем браузер после всех манипуляций
            browser.quit()
