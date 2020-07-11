from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ui.pages.module_base import ModuleBase
from selenium.webdriver.support.ui import Select
import time
import math
import os
from pathlib import Path

class ModuleTwo(ModuleBase):

    def task_2_part11(self):
        browser = self.driver()
        try:
            link = "http://suninjuly.github.io/math.html"

            browser.get(link)

            # Ваш код, который заполняет обязательные поля
            x = browser.find_element_by_id("input_value")
            x_value = x.text
            y = self.calc(x_value)
            # Отправляем заполненную форму
            browser.find_element_by_id("answer").send_keys(y)

            browser.find_element(By.XPATH, '//label[contains(text(), "I\'m the robot")]').click()

            browser.find_element(By.XPATH, '//label[contains(text(), "Robots rule")]').click()

            browser.find_element(By.XPATH, '//button').click()

        finally:
            # ожидание чтобы визуально оценить результаты прохождения скрипта
            time.sleep(5)
            # закрываем браузер после всех манипуляций
            browser.quit()

    def task_2_part12(self):
        browser = self.driver()
        try:
            link = "http://suninjuly.github.io/selects2.html"
            browser.get(link)

            # Ваш код, который заполняет обязательные поля
            value1 = browser.find_element_by_id("num1").text
            value2 = browser.find_element_by_id("num2").text
            result = int(value1) + int(value2)
            # Отправляем заполненную форму
            select = Select(browser.find_element_by_tag_name("select"))
            select.select_by_value(str(result))

            browser.find_element(By.XPATH, '//button').click()

        finally:
            # ожидание чтобы визуально оценить результаты прохождения скрипта
            time.sleep(5)
            # закрываем браузер после всех манипуляций
            browser.quit()

    def task_2_part21(self):
        browser = self.driver()
        try:
            link = "http://suninjuly.github.io/get_attribute.html"

            browser.get(link)

            # Ваш код, который заполняет обязательные поля
            img = browser.find_element_by_id("treasure")
            img_value = img.get_attribute("valuex")
            y = self.calc(img_value)
            # Отправляем заполненную форму
            browser.find_element_by_id("answer").send_keys(y)

            browser.find_element_by_id("robotCheckbox").click()

            browser.find_element_by_id("robotsRule").click()

            browser.find_element(By.XPATH, '//button').click()

        finally:
            # ожидание чтобы визуально оценить результаты прохождения скрипта
            time.sleep(5)
            # закрываем браузер после всех манипуляций
            browser.quit()

    def task_2_part22(self):
        browser = self.driver()
        try:
            link = "http://suninjuly.github.io/execute_script.html"

            browser.get(link)

            # Ваш код, который заполняет обязательные поля
            x = browser.find_element_by_id("input_value")
            x_value = x.text
            y = self.calc(x_value)
            # Отправляем заполненную форму
            browser.find_element_by_id("answer").send_keys(y)

            browser.find_element(By.XPATH, '//label[contains(text(), "I\'m the robot")]').click()

            checkbox = browser.find_element(By.XPATH, '//label[contains(text(), "Robots rule")]')
            browser.execute_script("return arguments[0].scrollIntoView(true);", checkbox)
            checkbox.click()

            browser.find_element(By.XPATH, '//button').click()

        finally:
            # ожидание чтобы визуально оценить результаты прохождения скрипта
            time.sleep(5)
            # закрываем браузер после всех манипуляций
            browser.quit()

    def task_2_part23(self):
        browser = self.driver()
        try:
            link = "http://suninjuly.github.io/file_input.html"

            browser.get(link)

            # Ваш код, который заполняет обязательные поля
            browser.find_element_by_name("firstname").send_keys("mikhail")
            browser.find_element_by_name("lastname").send_keys("volkov")
            browser.find_element_by_name("email").send_keys("volkov@mail.ru")
            p = Path(__file__).parents[1]
            file_path = os.path.join(p, 'test.txt')  # добавляем к этому пути имя файла
            browser.find_element_by_id("file").send_keys(os.path.join(file_path))
            # Отправляем заполненную форму
            browser.find_element(By.XPATH, '//button').click()

        finally:
            # ожидание чтобы визуально оценить результаты прохождения скрипта
            time.sleep(5)
            # закрываем браузер после всех манипуляций
            browser.quit()

    def task_2_part31(self):
        browser = self.driver()
        try:
            link = 'http://suninjuly.github.io/alert_accept.html'

            browser.get(link)

            browser.find_element_by_tag_name("button").click()

            browser.switch_to.alert.accept()

            x = browser.find_element_by_id("input_value")
            x_value = x.text
            y = self.calc(x_value)
            # Отправляем заполненную форму
            browser.find_element_by_id("answer").send_keys(y)
            browser.find_element(By.XPATH, '//button').click()

        finally:
            # ожидание чтобы визуально оценить результаты прохождения скрипта
            time.sleep(5)
            # закрываем браузер после всех манипуляций
            browser.quit()

    def task_2_part32(self):
        browser = self.driver()
        try:
            link = 'http://suninjuly.github.io/redirect_accept.html'

            browser.get(link)

            browser.find_element_by_tag_name("button").click()

            browser.switch_to_window(browser.window_handles[1])

            x = browser.find_element_by_id("input_value")
            x_value = x.text
            y = self.calc(x_value)
            # Отправляем заполненную форму
            browser.find_element_by_id("answer").send_keys(y)
            browser.find_element(By.XPATH, '//button').click()

        finally:
            # ожидание чтобы визуально оценить результаты прохождения скрипта
            time.sleep(5)
            # закрываем браузер после всех манипуляций
            browser.quit()

    def task_2_part41(self):
        browser = self.driver()
        try:
            link = 'http://suninjuly.github.io/explicit_wait2.html'

            browser.get(link)

            button = WebDriverWait(browser, 12).until(
                EC.text_to_be_present_in_element((By.ID, "price"), "$100")
            )
            browser.find_element_by_id("book").click()

            x = browser.find_element_by_id("input_value")
            x_value = x.text
            y = self.calc(x_value)
            # Отправляем заполненную форму
            browser.find_element_by_id("answer").send_keys(y)
            browser.find_element_by_id("solve").click()

        finally:
            # ожидание чтобы визуально оценить результаты прохождения скрипта
            time.sleep(5)
            # закрываем браузер после всех манипуляций
            browser.quit()
